# https://www.hackinscience.org/exercises/product-of-iterable

def mul(numbers):
    res=1
    for i in numbers:
        res *= i
    return res

if __name__ == "__main__":
    print(mul(range(1,6)))