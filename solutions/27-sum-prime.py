# https://www.hackinscience.org/exercises/sum-every-prime-number-below-n

import math

def is_prime(n):
    if n<=1:
        return False
        
    for i in range(2,math.floor(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    
    return True

def sum_primes(num):
    return sum([i for i in range(num) if is_prime(i)])

if __name__ == "__main__":
    print(sum_primes(10))