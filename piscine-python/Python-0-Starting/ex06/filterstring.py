import sys


def filter_words(S, N):
    """
    Accepts a string (S) and an integer (N) and returns a list of words
    from S that have a length greater than N.
    """

    words = S.split(' ')
    result_list = [word for word in words if
                   (lambda word_len_check: len(word_len_check) > N)(word)]

    return result_list


def main():
    """
    Main function to handle argument parsing and validation.
    """

    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    S_arg = sys.argv[1]
    N_arg = sys.argv[2]

    if not isinstance(S_arg, str):
        raise AssertionError("the arguments are bad")
    try:
        N = int(N_arg)
    except ValueError:
        raise AssertionError("the arguments are bad")
    result = filter_words(S_arg, N)
    print(result)


if __name__ == '__main__':
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
