#!/bin/python3
from ctf import *

def main(code):
	ctf(code)

if __name__ == "__main__":
	code = "qAp1nAiVtMkaCLmJNg4Q6f8szuFt2xjW"

	first_split = code[0:16][::-1]
	second_split = code[16:32]

	main("".join(x+y for x,y in zip(*(s+s[-1]*(max(len(second_split),len(first_split))-len(s)) for s in (second_split,first_split)))))
