import sys

def decipher(ciph_str, n):
	print("Deciphering the string: ", ciph_str, "\n")

	if (n == 3):
		print(ciph_str[::4])

def main():
	m_string = input("\nIntroduce the string to cipher using zig-zag method: ")
	m_rails = int(input("Introduce the number of rails (N): "))

	print("Ciphering...\n")

	# Clean the string from whitespaces
	m_string = m_string.replace(" ", "");

	if (m_rails == 3):
		print(m_string[::4])

		print(m_string[1:15][::2])

		print(m_string[2:15][::4])

		m_ciph_str = m_string[::4] +  m_string[1:15][::2] + m_string[2:15][::4]
		print("\nCiphered string: ", m_ciph_str, "\n")

		decipher(m_ciph_str, m_rails)


if __name__ == "__main__":
	main()