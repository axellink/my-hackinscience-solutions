# https://www.hackinscience.org/exercises/my-add

import sys

try:
    print(int(sys.argv[1]) + int(sys.argv[2]))
except:
    print(f"usage: python3 {sys.argv[0]} OP1 OP2")