# https://www.hackinscience.org/exercises/caesar-cypher

import string

# Not sure this is really readable, but hey
# I'm having fun at least ^^

def encrypt_car(c, key):
    base = ord('a') if c in string.ascii_lowercase else ord('A')
    return chr( ( (ord(c) - base + key) %26) + base)

def caesar_cypher_encrypt(s, key):
    return ''.join(
        encrypt_car(i, key) if i in string.ascii_letters else i 
        for i in s
    )

def caesar_cypher_decrypt(s, key):
    return caesar_cypher_encrypt(s, -key)