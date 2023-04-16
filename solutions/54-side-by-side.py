# https://www.hackinscience.org/exercises/side-by-side

from textwrap import wrap
from itertools import zip_longest

def sidebyside(left, right, width=79):
    in_width = (width-1)//2

    wrapped_left = wrap(left,in_width)
    wrapped_right = wrap(right,in_width)

    return "\n".join(
        f"{_left.ljust(in_width)}|{_right.ljust(in_width)}"
        for _left, _right 
        in zip_longest(wrapped_left, wrapped_right, fillvalue=" " * in_width)
    )