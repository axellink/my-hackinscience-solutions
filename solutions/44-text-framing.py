# https://www.hackinscience.org/exercises/text-framing

from dataclasses import dataclass, replace


@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"


fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")


def frame_text(text: str, frame: Frame) -> str:
    lines = text.split('\n')
    max_width = max(len(l) for l in lines)
    res = frame.top_left + (max_width * frame.top) + frame.top_right + '\n'
    for i in lines:
        res += frame.left + i + ((max_width-len(i)) * ' ') + frame.right + '\n'
    res += frame.bottom_left + (max_width * frame.bottom) + frame.bottom_right
    return res

if __name__ == "__main__":
    fir = """      *
     ***
    *****
   *******
    *****
   *******
  *********
 ***********
*************
     |||
     |||"""
    print(frame_text(fir, Frame()))
    print(frame_text(fir, fancy_frame))