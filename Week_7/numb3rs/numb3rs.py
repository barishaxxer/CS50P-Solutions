import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.search(pattern,ip))





if __name__ == "__main__":
    main()
