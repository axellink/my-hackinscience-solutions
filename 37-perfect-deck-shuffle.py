# https://www.hackinscience.org/exercises/perfect-deck-shuffle

def perfect_shuffle(deck):
    mid = len(deck)//2
    return sum([[i, deck[idx + mid]] for idx, i in enumerate(deck[:mid])],[])