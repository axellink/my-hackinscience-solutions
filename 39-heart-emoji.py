# https://www.hackinscience.org/exercises/hearts-emojis

from unicodedata import name

print(*[chr(i) for i in range(230000) if "HEART" in name(chr(i),"")])