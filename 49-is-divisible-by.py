# https://www.hackinscience.org/exercises/is-divisible-by

for i in range(0,1001):
    if i%7 == 0 and sum([int(i) for i in [*((i).__str__())]])%3==0:
        print(i)