def main():
    prompt = input("Greeting: ")
    print(f"${value(prompt)}")


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
