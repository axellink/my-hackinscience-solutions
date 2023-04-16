# https://www.hackinscience.org/exercises/roman-numerals

ROMAN={
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I':1
}

def to_roman_numeral(n):
    res = ""
    for roman, num in ROMAN.items():
        occ, n = divmod(n,num)
        res += occ * roman
    return res

if __name__ == "__main__":
    print(to_roman_numeral(1))
    print(to_roman_numeral(2))
    print(to_roman_numeral(4))
    print(to_roman_numeral(8))
    print(to_roman_numeral(16))
    print(to_roman_numeral(32))