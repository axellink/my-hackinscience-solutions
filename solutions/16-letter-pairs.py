# https://www.hackinscience.org/exercises/print-every-two-letters-pairs

from string import ascii_lowercase as lower_letter
[print(f"{i}{j}") for i in lower_letter for j in lower_letter]