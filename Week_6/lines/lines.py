import sys


def main():
    is_valid()
    print(lines_of_code(sys.argv[1]))


def is_valid():
    if len(sys.argv[1:]) > 1:
        sys.exit("too many arguments")
    elif len(sys.argv[1:]) < 1:
        sys.exit("too few arguments")
    elif not (sys.argv[1].endswith(".py")):
        sys.exit("not a python file")

def lines_of_code(file):
    x = 0
    try:
        with open(file) as f:
            for i in f:
                if i.strip() != "" and not (i.strip().startswith("#")):
                    x += 1
    except FileNotFoundError:
        sys.exit("file not found")
    return x




main()

