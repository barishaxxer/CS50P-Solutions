
def main():
    prompt = input("")
    print(shorten(prompt))


def shorten(word):
    return "".join([i if i not in ["A","E","I","O","U","a","e","i","u","o"] else "" for i in word])



if __name__ == "__main__":
    main()


