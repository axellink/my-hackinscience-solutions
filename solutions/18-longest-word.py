# https://www.hackinscience.org/exercises/longest-word

def longest_word(text):
    return max(text.split(), default='', key=len)