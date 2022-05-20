## [Topic: Cryptography] Misscalculated RSA

### Description
### We have found the password of the hacker but it's encrypted with a public key! It impossible to factorize the public key in order to crack the private key of an RSA... Wait, what does this generation configuration means? Maybe it is possible to crack it now...

Run pwn.py

Create a private key using the parameters obtained with the py file

./rsatool.py -n <obtained_n> -p <obtained_p> -q <obtained_q> -e <obtained_e) -f DER -o private_key.key

openssl pkeyutl -decrypt -in code.enc -out flag.txt -inkey private_key.key