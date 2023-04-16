# https://www.hackinscience.org/exercises/pernicious-numbers

import math

def is_prime(n):
    if n<=1:
        return False
        
    for i in range(2,math.floor(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    
    return True
    
print(*[
        n for n in range(222281, 222381)
        if is_prime(bin(n).count('1'))
    ],
    sep='\n')