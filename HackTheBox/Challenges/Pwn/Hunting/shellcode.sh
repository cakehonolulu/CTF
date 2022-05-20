#!/bin/sh

shellcode=$(objdump -d shellcode.o |grep '[0-9a-f]:'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\\x/g'|paste -d '' -s|sed "s/$/'/g"|sed "s/^/payload = b'/")
rm -f payload.py
echo $shellcode > payload.py