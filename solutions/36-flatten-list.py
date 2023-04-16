# https://www.hackinscience.org/exercises/flatten-lists

def flatten(a_list):
    return sum([[x] if not isinstance(x, list) else flatten(x) for x in a_list],[])