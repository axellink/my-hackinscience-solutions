# https://www.hackinscience.org/exercises/is-prime

import math


def is_prime(n):
    if n<=1:
        return False
        
    for i in range(2,math.floor(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    
    return True