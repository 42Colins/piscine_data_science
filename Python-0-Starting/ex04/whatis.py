import sys


def main():
    """Main function"""
    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided")
        sys.exit()
    elif not sys.argv[1].isdigit():
        if not (sys.argv[1][0] == '-' and sys.argv[1][1:].isdigit()):
            raise AssertionError("the argument is not an integer")
            sys.exit()

    value = int(sys.argv[1])
    if (value % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as err:
        print(f"AssertionError: {err}")
