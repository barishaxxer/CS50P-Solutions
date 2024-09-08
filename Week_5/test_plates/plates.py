def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum() and s[:2].isalpha():
        count = False
        for i in s:
            if i.isdigit() :
                if count == False and i == "0":
                    return False
                count = True
            elif count:
                return False
        return True

    else:
        return False



if __name__ == "__main__":
    main()
