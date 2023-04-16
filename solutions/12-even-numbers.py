# https://www.hackinscience.org/exercises/print-even-numbers

def print_even_numbers(start, stop):
    for i in range(start, stop):
        if i%2 == 0:
            print(i)

if __name__ == "__main__":
    print_even_numbers(10,50)