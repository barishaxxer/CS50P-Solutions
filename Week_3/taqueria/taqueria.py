def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    cost = 0
    while True:
        try:
            item = input("Item: ").strip().title()
            cost = cost + menu.get(item)
            print(f"Total: ${cost:.2f}")
        except TypeError:
            pass
        except EOFError:
            break

main()
