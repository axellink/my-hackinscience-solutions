# https://www.hackinscience.org/exercises/format-your-output

def list_pretty_print(items):
    step = len(items)//5
    for i in range(step):
        print(*items[i*5:(i+1)*5], sep=', ')
    print(*items[step*5:], sep=', ')

if __name__ == "__main__":
    list_pretty_print(range(12))