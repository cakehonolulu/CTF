#!/usr/bin/env bash

DEBUG=1

# Function that prints this script's usage
function usage {
    echo -e "\e[32mUsage:\e[39m"
    echo -e "./find_acc.sh \e[1m[FLAG]\e[0m"
    echo ""
    echo -e "\e[1mFLAG:\e[0m    String containing the FLAG to search for"
    echo -e "\e[1mLOGFILE:\e[0m Log file containing the list of requests to analyze"
    echo ""
    echo -e "\e[34mExample:\e[39m"
    echo "./find_acc.sh FLAG{s3c8r3_l0g}"
    echo "Searches for the string 'FLAG{s3c8r3_l0g}' in the requests file"
    echo ""
    echo "./find_acc.sh FLAG{n\/we_C7F} web_requests.log"
    echo "Searches for the string 'FLAG{n\/we_C7F}' in the 'web_requests.log' file"
    exit 1
}

# Check if more that 2 arguments specified
if [ $# -ge 3 ] ; then
    echo -e "[\e[31mX\e[39m] More than 2 arguments specified!"
    echo ""
    usage
fi

# Check for no arguments specified
if [[ $# -eq 0 ]] ; then
    usage
fi

# Check if second argument exists
if [ "$2" ]; then
    # If it does, then that's *probably* the log file; check if it exists
    if test -f "$2"; then
        # If it does, assign it to a variable
        logfile=$2
        echo -e "[\e[90m*\e[39m] Using the log file $logfile ...";
    else 
        # If it doesn't, warn the user and exit
        echo -e "[\e[31mX\e[39m] The log file you specified doesn't exists!"
        exit 1
    fi
else
    # If there's no second argument, assume the regular log file name (http_server.log)
    logfile="http_server.log"
    echo -e "[\e[90m*\e[39m] Using the default log file (http_server.log) ...";
fi

# Regex with possible user list
possible_users='admin|info|michael|john|david|robert|chris|mike|dave|richard|thomas|steve|mark|andrew|daniel|george|paul|charlie|dragon|james|qwerty|martin|master|mail|charles|bill|patrick|peter|shadow|johnny'

echo -e "[\e[90m*\e[39m] Searching $1 in requests";

# Convert the script's argument (Which is the flag) to base64 (First removing the newline)
b64flag=$(echo $1 | tr -d '\n' | base64)

# If debug is 1, print the base64 encoded flag
if [ "$DEBUG" == "1" ]; then
    echo -e "[\e[94mD\e[39m] \e[1mOriginal flag:\e[0m $1; \e[1mBase64 Encoded:\e[0m $b64flag"
fi

# URL-Encode the Base64 representation, focus only on swapping '=' with '%3D'; sed does this in a clean and simple way
url_enc_flag=$(echo $b64flag | sed "s/=/%3D/g")

# If debug is 1, print the URL encoded flag
if [ "$DEBUG" == "1" ]; then
    echo -e "[\e[94mD\e[39m] \e[1mURL-Encoded:\e[0m $url_enc_flag"
fi

# During the entire search in the log file for the Base64-enc flag, store last username found in awk's found_user, they'll get overwritten until the last one (Hacked one) is found
offender_request=$(cat "$logfile" | awk '/'$possible_users'/ {found_user=$0} /'$url_enc_flag'/ {print found_user}')

# Check if we found the request (Or there was an error)
if [ -z "$offender_request" ]; then
    echo -e "[\e[31mX\e[39m] Could not find the offending request, exiting..."
    exit 1
fi

# If debug is 1, print the request
if [ "$DEBUG" == "1" ]; then
    echo -e "[\e[94mD\e[39m] \e[1mOffending request:\e[0m $offender_request"
fi

# Prettify the output, assign the matched user from the reg-ex to a variable in order to print it prettier
pwned_user=$(echo $offender_request | grep -oE $possible_users)

if [ -z "$pwned_user" ]; then
    echo -e "[\e[31mX\e[39m] Could not process the request, exiting..."
    exit 1
fi

# Print the pwned user
echo -e "[\e[32m!\e[39m] Found the pwned user: $pwned_user"
