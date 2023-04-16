# https://www.hackinscience.org/exercises/is-prime

import math


def is_prime(n):
    if n<=1:
        return False
        
    for i in range(2,math.floor(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    
    return True

if __name__ == "__main__":
    print(is_prime(6))
    print(is_prime(13))
    print(is_prime(197))