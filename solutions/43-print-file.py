# https://www.hackinscience.org/exercises/print-the-content-of-the-file-words

with open("words.txt", "r") as f:
    print(f.read())