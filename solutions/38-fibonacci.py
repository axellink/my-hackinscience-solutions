# https://www.hackinscience.org/exercises/fibonacci-sequence

from functools import cache

@cache
def _fibonacci(n):
    return 1 if n<2 else _fibonacci(n-1) + _fibonacci(n-2)

def fibonacci(n):
    return [_fibonacci(i) for i in range(n)]

if __name__ == "__main__":
    print(fibonacci(3))
    print(fibonacci(5))
    print(fibonacci(10))