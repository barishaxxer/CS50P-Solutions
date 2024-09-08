def main():
    camel = input("camelCase: ").strip()
    print("snake_case:",snake_case(camel))


def snake_case(camelCase):
    a = ""
    for n,i in enumerate(camelCase):
        if i.isupper():
            i = "_" + i
        a = a + i
    return a.lower()
main()
