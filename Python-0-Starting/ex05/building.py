import sys


def isPunctuation(char):
    """Is it punctuation ?"""
    punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    for mark in punctuation:
        if char == mark:
            return 1
    return 0


def count_characters(string):
    """A function counting each characters in a string
    (char, numbers, space, punctuation)"""
    i = 0
    lowercase_count, uppercase_count, number_count = 0, 0, 0
    space_count, punctuation_count = 0, 0
    for char in string:
        if char.isdigit():
            number_count += 1
        elif char.isalpha():
            if char.islower():
                lowercase_count += 1
            else:
                uppercase_count += 1
        elif char.isspace():
            space_count += 1
        elif isPunctuation(char):
            punctuation_count += 1
        i += 1

    print("The text contains", i, "characters")
    print(uppercase_count, "upper letters")
    print(lowercase_count, "lower letters")
    print(punctuation_count, "punctuation marks")
    print(space_count, "spaces")
    print(number_count, "digits")


def main():
    """MAIN Function"""
    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 1:
        value = sys.stdin.readline()
    else:
        value = sys.argv[1]
    count_characters(value)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as err:
        print(f"AssertionError: {err}")
