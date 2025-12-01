import sys

a = int(10)
if (len(sys.argv) > 2):
    print("AssertionError: more than one argument is provided")
    sys.exit()
elif not sys.argv[1].isdigit():
    if not (sys.argv[1][0] == '-' and sys.argv[1][1:].isdigit()):
        print("AssertionError: argument is not an integer")
        sys.exit()

value = int(sys.argv[1])
if (value % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
