#include <stdio.h>
#include <unistd.h>
#include <stdint.h>

int main(int argc, char **argv)
{
    long local_10 = 0x53e5854620fb399f;
    long local_18 = 0x576b96b95df201f9;
    char m_buffer[32];
    printf("\n[*] Current target\'s coordinates: x = [0x%lx], y = [0x%lx]\n\n[*] Insert new coordinate s: x = [0x%lx], y = ", 0x53e5854620fb399f, 0x576b96b95df201f9, 0x53e5854620fb399f);
    read(0,m_buffer,31);
    printf("\n[*] New coordinates: x = [0x53e5854620fb399f], y = %s\n[*] Verify new coordinates? (y/n) : ", m_buffer);
    return 0;
}
