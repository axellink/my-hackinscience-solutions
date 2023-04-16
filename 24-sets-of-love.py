# https://www.hackinscience.org/exercises/sets-of-love

def love_meet(bob, alice):
    return set(bob).intersection(set(alice))


def affair_meet(bob, alice, silvester):
    return set(alice).intersection(set(silvester)) - set(bob)