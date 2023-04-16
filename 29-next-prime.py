# https://www.hackinscience.org/exercises/print-the-first-prime-number-after-the-given-one

import math
import itertools

def is_prime(n):
    if n<=1:
        return False
        
    for i in range(2,math.floor(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    
    return True

for i in itertools.count(100000000):
    if is_prime(i):
        print(i)
        break