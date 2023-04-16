# https://www.hackinscience.org/exercises/lambda-expressions

def filtered(items, filter_func):
    return [item for item in items if filter_func(item)]
    
print(str(filtered(range(101), lambda x: x%3 == 0))[1:-1])
print(str(filtered(range(101), lambda x: x%5 == 0))[1:-1])
print(str(filtered(range(101), lambda x: x%15 == 0))[1:-1])