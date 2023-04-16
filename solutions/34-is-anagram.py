# https://www.hackinscience.org/exercises/is_anagram

import re

def normalize(string):
    norm = string.lower()
    norm = re.sub(r'[àáâãäå]', 'a', norm)
    norm = re.sub(r'[èéêë]', 'e', norm)
    norm = re.sub(r'[ìíîï]', 'i', norm)
    norm = re.sub(r'[òóôõö]', 'o', norm)
    norm = re.sub(r'[ùúûü]', 'u', norm)
    norm = re.sub(r'[ç]', 'c', norm)
    norm = re.sub(r'[-\/\'_ ]', '', norm)
    return norm

def is_anagram(left, right):
    n_left = list(normalize(left))
    n_right = list(normalize(right))
    n_left.sort()
    n_right.sort()
    return n_left == n_right