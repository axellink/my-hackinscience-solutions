# https://www.hackinscience.org/exercises/reverse-roman-numerals

ROMAN_NUM = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def from_roman_numeral(roman_numeral):
    res = 0
    i = 0
    while i < len(roman_numeral):
        if (
            i == len(roman_numeral) - 1
            or ROMAN_NUM[roman_numeral[i]] >= ROMAN_NUM[roman_numeral[i+1]]
        ):
            res += ROMAN_NUM[roman_numeral[i]]
        else:
            res += ROMAN_NUM[roman_numeral[i+1]] - ROMAN_NUM[roman_numeral[i]]
            i += 1
        i += 1
    return res

if __name__ == "__main__":
    print(from_roman_numeral("V"))
    print(from_roman_numeral("XX"))
    print(from_roman_numeral("DCCC"))
    print(from_roman_numeral("MMMM"))