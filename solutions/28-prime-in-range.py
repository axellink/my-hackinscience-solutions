# https://www.hackinscience.org/exercises/print-every-prime-numbers-in-a-range

import math

def is_prime(n):
    if n<=1:
        return False
        
    for i in range(2,math.floor(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    
    return True

print(', '.join([str(i) for i in range (10000,10050) if is_prime(i)]))