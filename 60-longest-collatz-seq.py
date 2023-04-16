# https://www.hackinscience.org/exercises/longest-collatz-sequence

def collatz_length(n):
    i = 0
    while n > 1:
        i += 1
        n = n//2 if n%2 == 0 else (n*3)+1
    return i