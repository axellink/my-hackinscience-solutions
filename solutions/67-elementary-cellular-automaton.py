import sys

def usage() -> None:
    """
    Print the usage
    """
    print(f"Usage : {sys.argv[0]} [PARAM]")
    print(f"PARAM : integer beween 0 and 255")

def do_the_job(parameter, steps=40, size=79):
    if size%2 == 0:
        raise ValueError("Size must be odd")

    state = [0] * (size//2) + [1] + [0] * (size//2)

    for _ in range(steps):
        print("".join(["#" if i else "." for i in state]))
        new_state = [parameter >> int(f"{state[i-1]}{state[i]}{state[(i+1)%size]}",2) & 1
                     for i in range(size)]
        state = new_state

if __name__ == "__main__":
    try:
        parameter = int(sys.argv[1])
        if parameter<0 or parameter>255:
            raise ValueError()
        else:
            do_the_job(parameter)
    except Exception as e:
        usage()
        sys.exit(1)