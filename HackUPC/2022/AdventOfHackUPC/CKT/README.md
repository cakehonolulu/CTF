## Reverse engineering: Cocktail

### Description
### The code is inside this program, can you find it?  

Original code:

 import sys


def main(code):
 new_code = change(code)
 if new_code == "qAp1nAiVtMkaCLmJNg4Q6f8szuFt2xjW":
  print("Code found! Advent{%s}" % code)
 else:
  print("No")

def change(code):
 return code[::-2] + code[::2]

if __name__ == "__main__":
 main(sys.argv[1])
