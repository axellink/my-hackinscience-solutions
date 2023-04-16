# https://www.hackinscience.org/exercises/longest-word

def longest_word(text):
    return max(text.split(), default='', key=len)

if __name__ == "__main__":
    print(longest_word("We want a SHRUBBERY"))