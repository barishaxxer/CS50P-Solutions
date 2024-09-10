due = 50
while due > 0:
    print("Amount Due:", due)

    inserted = int(input("Insert Coin: "))

    if inserted == 25 or inserted == 10 or inserted == 5:
        if (due - inserted) < 0:
            print("Change Owed:", inserted - due)
            break
        elif (due - inserted) == 0:
            print("Change Owed:", 0)
            break
        else:
            due = due - inserted
    else:
        pass
