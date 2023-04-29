from string import ascii_uppercase
from random import choice

def gen_colors(code_size: int) -> str:
    return ascii_uppercase[:code_size]

def gen_code(code_size: int, colors: str) -> str:
    return "".join([choice(colors) for i in range(code_size)])

def check_guess(guess, code_size, colors) -> bool:
    return len(guess) == code_size and not set(guess) - set(colors)

def score_guess(code, guess):
    all_good = 0
    color_good = 0
    left_in_code = []
    left_in_guess = []
    for i in range(len(code)):
        if code[i] == guess[i]:
            all_good += 1
        else:
            left_in_code += [code[i]]
            left_in_guess += [guess[i]]
    for i in left_in_guess:
        if i in left_in_code:
            color_good += 1
            left_in_code.remove(i)
    return (all_good, color_good)

def play_cli(code_size, nb_colors):
    colors = gen_colors(nb_colors)
    code = gen_code(code_size, colors)
    attempt = 0
    print(f"Possible colors are {colors}")
    print(f"Code is size 4")
    while True:
        guess = input(f"{attempt} -->")

        if not check_guess(guess, code_size, colors):
            print("Wrong size or color !")
            continue

        attempt += 1
        all_good, color_good = score_guess(guess, code)
        
        if all_good == code_size:
            break

        print(f"({all_good}, {color_good})")
    print(f"Congrats, you won after {attempt} attempts !")


if __name__ == "__main__":
    play_cli(4,6)
#    code_size = 4
#    colors = gen_colors(6)
#    print(gen_code(code_size, colors))
#
#    assert(check_guess("AFDE", code_size, colors))
#    assert(not check_guess("AFDED", code_size, colors))
#    assert(not check_guess("AFDG", code_size, colors))
#
#    print(score_guess("ABCD", "ABCD"))
#    print(score_guess('AAAA', 'ABCD'))
#    print(score_guess('AADA', 'ABCD'))
#    print(score_guess('ADDA', 'ABCD'))
#    print(score_guess('ADDB', 'ABCD'))