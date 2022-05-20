
all: clean
	-@clang shellcode.S --target=i386-unknown-linux-gnu -march=i386 -nostdlib -ffreestanding -fno-builtin -o shellcode.o
	-@./shellcode.sh
	-@./exploit.py

clean:
	-@rm -f payload.py
	-@rm -f shellcode.o
