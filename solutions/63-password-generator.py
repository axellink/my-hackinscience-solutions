# https://www.hackinscience.org/exercises/password-generator

from string import ascii_lowercase, ascii_uppercase, digits
from random import choice, shuffle

def pwgen(length, with_digits = True, with_uppercase = True):
    charset = ascii_lowercase
    res = [choice(ascii_lowercase)]
    length -= 1

    if with_uppercase:
        res += [choice(ascii_uppercase)]
        charset += ascii_uppercase
        length -= 1
    
    if with_digits:
        res += [choice(digits)]
        charset += digits
        length -= 1

    if length < 0:
        raise ValueError("Not long enough for categories asked")
    
    for _ in range(length):
        res += [choice(charset)]
    
    shuffle(res)
    return ''.join(res)


if __name__ == "__main__":
    print(pwgen(4))
    print(pwgen(4, with_digits=False))
    print(pwgen(4, with_uppercase=False))
    print(pwgen(4, with_uppercase=False, with_digits=False))
