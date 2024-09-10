import random


def main():
    correct = 0

    lvl = get_level()
    for n in range(10):
        x, y = generate_integer(lvl), generate_integer(lvl)
        for i in range(3):
            answer = input(str(x) + " + " + str(y) + " = ")
            if int(answer) == x + y:
                correct += 1
                break
            else:
                print("EEE")
            if i == 2:
                print(f"{x} + {y} = {x + y}")
                break
            pass
        if n == 9:
            print("Score:", correct)


def get_level():
    while True:

        try:
            level = int(input("Level: "))
            if not (0 < level < 4):
                pass
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    range_start = 10 ** (level - 1)
    range_end = (10**level) - 1
    if level == 1:
        return random.randint(0, range_end)
    else:
        return random.randint(range_start, range_end)


if __name__ == "__main__":
    main()
