# https://www.hackinscience.org/exercises/draw-n-squares

def draw_n_squares(n):
    res = ""
    for i in range(n):
        res += "+---" * n + "+\n"
        res += "|   " * n + "|\n"
    res += "+---" * n + "+\n"
    return res

if __name__ == "__main__":
    print(draw_n_squares(1))
    print(draw_n_squares(3))
    print(draw_n_squares(10))