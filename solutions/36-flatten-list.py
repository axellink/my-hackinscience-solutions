# https://www.hackinscience.org/exercises/flatten-lists

def flatten(a_list):
    return sum([[x] if not isinstance(x, list) else flatten(x) for x in a_list],[])

if __name__ == "__main__":
    print(flatten([[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]))