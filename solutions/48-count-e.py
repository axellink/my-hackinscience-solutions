# https://www.hackinscience.org/exercises/count-the-lower-e-in-the-words-file

count = 0
with open("words.txt","r") as f:
    for l in f:
        count += l.count('e')
print(count)