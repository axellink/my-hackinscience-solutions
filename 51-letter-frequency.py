# https://www.hackinscience.org/exercises/give-the-frequency-of-letters-in-the-words-file

import string

count_char = dict()
num_char = 0
with open("words.txt") as f:
    while char := f.read(1):
        if char in string.ascii_lowercase:
            if char not in count_char.keys():
                count_char[char] = 1
            else:
                count_char[char] += 1
        num_char += 1

if num_char > 0:
    for letter, occurence in count_char.items():
        print(f"{letter}: {occurence/num_char:.2f}")