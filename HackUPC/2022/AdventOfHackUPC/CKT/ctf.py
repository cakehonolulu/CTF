import sys

def ctf(code):
	new_code = change(code)
	
	if new_code == "qAp1nAiVtMkaCLmJNg4Q6f8szuFt2xjW":
		print("Code found! Advent{%s}" % code)
	else:
		print("No")

def change(code):
	# qAp1nAiVtMkaCLmJ -> reversed JmLCakMtViAn1pAq
	# Ng4Q6f8szuFt2xjW -> reversed Wjx2tFuzs8f6Q4gN

	# Reverse first part and add second part
	# NJgm4LQC6afk8MstzVuiFAtn21xpjAWq

	return code[::-2] + code[::2]
