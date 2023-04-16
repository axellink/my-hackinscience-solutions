# https://www.hackinscience.org/exercises/sets-of-love

def love_meet(bob, alice):
    return set(bob).intersection(set(alice))


def affair_meet(bob, alice, silvester):
    return set(alice).intersection(set(silvester)) - set(bob)

if __name__ == "__main__":
    alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
    bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']
    silvester = ['XVII', 'XIX', 'III', 'I', 'III', 'XVII']

    print(love_meet(bob, alice))
    print(affair_meet(bob, alice, silvester))