import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        pattern = r'^<iframe(?:.*)? src="https?:\/\/(?:www\.)?youtube\.com\/embed\/(\w+)(.*)?><\/iframe>'
        match = re.search(pattern,s).group(1)
        return f"https://youtu.be/{match}"
    except AttributeError:
        return None
if __name__ == "__main__":
    main()
