# https://www.hackinscience.org/exercises/product-of-iterable

def mul(numbers):
    res=1
    for i in numbers:
        res *= i
    return res