#!/usr/bin/python3

import sys
import datetime
import random
import string
import socket
import struct
import base64
import urllib.parse


# List of usernames
usernames = [
        "",
        "admin",
        "info",
        "michael",
        "john",
        "david",
        "robert",
        "chris",
        "mike",
        "dave",
        "richard",
        "thomas",
        "steve",
        "mark",
        "andrew",
        "daniel",
        "george",
        "paul",
        "charlie",
        "dragon",
        "james",
        "qwerty",
        "martin",
        "master",
        "mail",
        "charles",
        "bill",
        "patrick",
        "peter",
        "shadow",
        "johnny" ]

# Random IP
random_ip= [ socket.inet_ntoa(struct.pack('>I',random.randint(1,0xffffffff))) for i in range (0,151)] 

# Endpoint definition  [GET, POST, PUT, DELETE, HAS_QUERY, QUERY ]
endpoints = { "/login": [["POST"],[200,302,403], "?token="],
              "/logout" : [["POST"], [200,302]],
              "/product" : [["GET","DELETE"],[200,403,404],"?productId="],
              "/dashboard" : [["GET"],[302,403], "?user="],
              "/index.html" : [["GET"], [200]]
             }

# HTTP Code Status
random_status = [200, 302, 404, 403, 500 ]

# Number of possilbe ID products
product_ids = [ x for x in range(1,201)] # 1-200

# User definition (username,userid)
users = [ [x, usernames[x]]  for x in range(1,len(usernames))] 

def create_legal_req( ):
    """
        Generates a legal request at random using different predefined variables.
        It is used to simulate real life user interaction with the server via HTTP


        returns 
            @final_request_0 IP and Username formated
            @final_request_1 Raw http method request with status code and data size
    """
    ip = random_ip[random.randint(0,len(random_ip) - 2 )]
    user_name = usernames[random.randint(0,len(usernames) - 1)]  
   
    rdm_key= random.choice(list(endpoints))
    rdm_endpoint = endpoints[rdm_key]
    rdm_http_method = random.randint(0,len(rdm_endpoint[0]) - 1)
    http_req = "{} {}".format(rdm_endpoint[0][rdm_http_method], rdm_key)  

    if len(rdm_endpoint) == 3: 
        http_req +="{}{}".format(rdm_endpoint[2],urllib.parse.quote_plus(generate_random_token()))
    http_method = "HTTP/1.1"
    
    status = random_status[random.randint(0,len(rdm_endpoint[1]) - 1)]

    data_size = random.randint(100,4001)
    
    final_request_0 = "{} -  {}".format(ip, user_name) # IP - user_name
    final_request_1 = "\"{} {}\" {} {}".format(http_req, http_method, status, data_size)
    
    return [final_request_0, final_request_1] 

def create_hacker_req():
    """
        Generates a illegal request at random using different predefined variables.
        It is used to simulate an attacker bruteforcing a login page via query ?token=

        returns 
            @final_request_0 IP and Username formated
            @final_request_1 Raw http method request with status code and data size
    """
    attacant_ip = random_ip[-1] 
    user_name = "-"
    http_req = "POST /login?token={}".format(urllib.parse.quote_plus(generate_random_token()))
    http_method = "HTTP/1.1"
    status = "403"
    data_size = random.randint(200,237)
    
    final_request_0 = "{} -  {}".format(attacant_ip, user_name) # IP - user_name
    final_request_1 = "\"{} {}\" {} {}".format(http_req, http_method, status, data_size)
    
    return [final_request_0,final_request_1] 

def create_flag_req(flag):
    """
        Generates the FLAG request, it contains the FLAG.
        It is important to notice that it has an status of 200

        returns 
            @final_request_0 IP and Username formated
            @final_request_1 Raw http method request with status code and data size
    """
    attacant_ip = random_ip[-1]
    user_name = "-"
    token = base64.b64encode(bytes(flag, "utf-8")).decode("utf-8")
    http_req = "POST /login?token={}".format(urllib.parse.quote_plus(token))
    http_method = "HTTP/1.1"
    status = "200"
    data_size = random.randint(200,237)
    
    final_request_0 = "{} -  {}".format(attacant_ip, user_name) # IP - user_name
    final_request_1 = "\"{} {}\" {} {}".format(http_req, http_method, status, data_size)
    
    return [final_request_0,final_request_1] 
    
def generate_random_string(length):
    """
        Generates a random string based on the argument @length
        returns
            @result_str Random string of lenght @lenght
    """
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_random_token():
    """
        Generates a random token in base64 from a random generated string
        returns
            @token random string encoded in base64
    """
    res= generate_random_string(16)
    return base64.b64encode(bytes(res,"utf-8")).decode("utf-8")

def print_req(moment_time, f_0, f_1):
    print("{} {} {}\n".format(f_0,  moment_time.strftime("[%d/%m/%Y:%H:%M:%S UTC+2]"), f_1))

##### Format example ######
# 10.251.17.1 - admin/- [10/Oct/2000:13:55:36 UTC+2] "GET /login HTTP/1.1" 200 <data_size_bytes>i
## Time : 22 March 2022 18:03 -> 19:43 -> 100 min -> 6000 seg -> 300.000 / 6000 -> 50 peticiones por segundo
## 74% attacant - 26% legal 

def main(total=100000, flag="FLAG{s3c8r3_l0g}", span_time=2):
    """
        Main function.

        Creates a log file with randomly generated requests simulating a login bruteforce attack. 
        There is one successful attack which contains the flag

    """

    print("Creating logs with ~{} lines, with flag {} and span_time {} seconds".format(total, flag, span_time))
    
    c_p_s = int(total / span_time) # HTTP request/second
    flag_dice = random.randint(0,c_p_s * span_time) # Line of flag
    print("FLAG generated at line {}".format(flag_dice))

    counter_hacker = 0 
    counter_legal = 0
    counter_flag = 0
    moment = datetime.datetime(2022,3,22,18,3,0) 

    log_file = open("http_server.log", "w")
    line_add = ""

    for i in range(1, span_time + 1): ## 0 - 5  
        moment = moment + datetime.timedelta(seconds=1)
        for j in range(c_p_s): ### HTTP request/second
            # Create request based on statistic
            dice = random.randint(0,10)
            if dice <= 7: 
                counter_hacker += 1
                f_0, f_1 = create_hacker_req()
            else:
                counter_legal += 1
                f_0, f_1 = create_legal_req()
            # Randomly add a flag
            if not counter_flag:
                if ((counter_hacker + counter_legal) == flag_dice):
                    f_0,f_1 = create_flag_req(flag)
                    counter_flag = 1
            line_add = "{} {} {}\n".format(f_0, moment.strftime("[%d/%m/%Y:%H:%M:%S UTC+2]"), f_1)
            log_file.write(line_add)


if __name__ == "__main__":
    if len(sys.argv) > 4 or (len(sys.argv) > 1 and sys.argv[1] == "-h") :
        print("Arguments {}".format(len(sys.argv)))
        raise SystemExit("Usage :python3 {} [<total_lines> <flag:Str> <span_time>]".format(sys.argv[0]))
    try:
        if len(sys.argv) == 1:
            main() 
        if len(sys.argv) == 2:
            main(int(sys.argv[1])) 
        if len(sys.argv) == 3:
            main(int(sys.argv[1]), sys.argv[2])
        if len(sys.argv) == 4:
            main(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    except:
        raise SystemExit("Usage :python3 {} [<total_lines:Int> <flag:Str> <span_time:Int>]".format(sys.argv[0]))
