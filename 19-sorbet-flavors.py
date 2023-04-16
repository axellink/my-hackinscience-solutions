# https://www.hackinscience.org/exercises/print-sorbet-flavors

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

# [print(f"{i}, {j}") for i in FLAVORS for j in FLAVORS[FLAVORS.index(i)+1:]]

offset=1
for i in FLAVORS:
    for j in FLAVORS[offset:]:
        print(f"{i}, {j}")
    offset += 1