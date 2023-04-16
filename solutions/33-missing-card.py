# https://www.hackinscience.org/exercises/the-missing-card

ALL_CARDS = {
    f"{i}{j}" 
    for i in {"S", "H", "D", "C"} 
    for j in {"2", "3", "4", "5", "6", "7", "8", "9", 
              "10", "J", "Q", "K", "A"}
}

def missing_card(cards):
    _cards = set(cards.split())
    return (ALL_CARDS - _cards).pop()