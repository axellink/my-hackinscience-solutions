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

if __name__ == "__main__":
    left = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed non risus. "
        "Suspendisse lectus tortor, dignissim sit amet, "
        "adipiscing nec, utilisez sed sin dolor."
    )

    right = (
        "Morbi venenatis, felis nec pretium euismod, "
        "est mauris finibus risus, consectetur laoreet "
        "sem enim sed arcu. Maecenas sit amet eleifend sem. "
        "Nullam ac libero metus. Praesent ac finibus nulla, vitae molestie dolor."
        " Aliquam vestibulum viverra nisl, id porta mi viverra hendrerit."
        " Ut et porta augue, et convallis ante."
    )

    print(sidebyside(left, right))
    print()
    print(sidebyside(left, right, 50))
    print()
    print(sidebyside(left, right, 100))
    print()
    print(sidebyside(left, sidebyside(left, left, 50), 100))