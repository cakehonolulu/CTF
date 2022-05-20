## Binary problem: Byte per byte

### Description
### The code is inside the binary code of this binary following this structure: Advent{code}. Good luck! 

You can use any hexadecimal viewer and glance through the file.

I used IDA64 and found references in main() to .bss; used the code graph to view each section and between .bss and .data found the flag (Offset: 0x3020)
