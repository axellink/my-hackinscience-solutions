# https://www.hackinscience.org/exercises/draw-n-squares

def draw_n_squares(n):
    res = ""
    for i in range(n):
        res += "+---" * n + "+\n"
        res += "|   " * n + "|\n"
    res += "+---" * n + "+\n"
    return res