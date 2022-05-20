#!/usr/bin/python3

from math import isqrt

from Crypto.Util.number import isPrime

from Crypto.PublicKey import RSA

def recover_a_b(n, number_of_bits, ab):
    bits = number_of_bits // 4
    # n = ((A * B) << bits * 2) + (A * B) + ((A * A + B * B) << bits)
    potential_a2b2 = (n - (ab << bits * 2) - ab) >> bits
    a2_plus_b2 = potential_a2b2 + 2 * ab
    if a2_plus_b2 >= 0:
        a_plus_b = isqrt(a2_plus_b2)
        if a_plus_b ** 2 == a2_plus_b2:
            X = a_plus_b
            Y = ab
            # a+b = X
            # a*b = Y
            # a = X-b
            # -b^2 + bX -Y = 0
            delta = X ** 2 - 4 * Y
            if delta >= 0:
                b0 = (-X - isqrt(delta)) // (-2)
                a0 = X - b0
                if a0 * b0 == ab and a0 + b0 == a_plus_b:
                    return a0, b0
                b1 = (-X + isqrt(delta)) // (-2)
                a1 = X - b1
                if a1 * b1 == ab and a1 + b1 == a_plus_b:
                    return a1, b1

def recover_p_q(n, number_of_bits, calculated_a_by_b):
    bits = number_of_bits // 4
    high = n >> (bits * 3)
    low = n & (2 ** bits // 2 - 1)
    for overflow in range(-256, 256):
        recovered_ab = ((high + overflow) << bits) + low
        res = recover_a_b(n, number_of_bits, calculated_a_by_b)
        if res:
            A, B = res
            p = A + (B << bits)
            q = B + (A << bits)
            if isPrime(p) and isPrime(q):
                return q, p

def main():
    public_key = RSA.importKey(open('pubkey.pem', 'r').read())
    n = public_key.n
    number_of_bits = 2048

    second_half_a_by_b = bin(public_key.n)[2:][1536:]

    first_half_a_by_b = bin(((int(bin(public_key.n)[2:][0:512], 2)) - 1))[2:]

    calculated_a_by_b = int(first_half_a_by_b + second_half_a_by_b, 2)

    print("Calculated A by B:\n", int(calculated_a_by_b), "\n")
    
    print("Length of N:\n", len(str(n)), "\n")
    
    p, q = recover_p_q(n, number_of_bits, calculated_a_by_b)

    if ((p * q) == n):
        print("Found N:\n", hex(p * q), "\n\n", "Found P:\n", hex(p), "\n\n", "Found Q:\n", hex(q), "\n\n", "E:\n", hex(public_key.e))
    elif ((p * q) != n):
        print("P and Q primitives are faulty, exiting...")

main()
