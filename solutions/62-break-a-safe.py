# https://www.hackinscience.org/exercises/break-a-safe

def generator(length, base):
    res = [0] * length
    while not all([i == base-1 for i in res]):
        yield res
        res[0] += 1
        for i in range(length-1):
            if res[i] == base:
                res[i+1] += 1
                res[i] = 0
    yield [base-1] * length
    
digits = [1,5,8]
for gen in generator(4,3):
    if len(set(gen)) == 3:
        print(*[digits[n] for n in gen])