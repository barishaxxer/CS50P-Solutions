from validator_collection import checkers


def main():
    x = checkers.is_email(input("whats email: "))
    if x:
        print("valid")
    else:
        print("invalid")


main()
