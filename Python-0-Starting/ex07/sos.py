import sys


MORSE_CODE = {
    " ": "/ ",  # Space separator
    # Letters
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    # Digits
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    # Punctuation
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "!": "-.-.--",
    ":": "---...",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
}


def main():
    """Main function"""
    try:
        if (len(sys.argv) != 2):
            raise AssertionError("the arguments are bad")

        S_arg = sys.argv[1]
        if not isinstance(S_arg, str):
            raise AssertionError("the arguments are bad")
        for char in S_arg:
            if char.upper() not in MORSE_CODE:
                raise AssertionError("the arguments are bad")
                return
    except AssertionError as err:
        print(f"AssertionError: {err}")
        return
    result = ' '.join(MORSE_CODE.get(char.upper(), '') for char in S_arg)
    print(result)


if __name__ == "__main__":
    main()
