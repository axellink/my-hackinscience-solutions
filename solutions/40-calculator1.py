# https://www.hackinscience.org/exercises/calculator1

import sys

OP={
    "+": lambda x, y : x + y,
    "-": lambda x, y : x - y,
    "*": lambda x, y : x * y,
    "/": lambda x, y : x / y,
    "^": lambda x, y : x ** y,
    "%": lambda x, y : x % y
}

if len(sys.argv) != 4:
    print(f"usage: {sys.argv[0]} a_number (an_operator +-*/%^) a_number")
    sys.exit()

try:
    print(OP[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3])))
except Exception:
    print("input error")