# https://www.hackinscience.org/exercises/print-the-first-parameter

import sys

if len(sys.argv) <= 1:
    print(f"usage: python3 {sys.argv[0]} PARAM", file=sys.stderr)
else:
    print(sys.argv[1])