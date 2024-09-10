exp = input("Expression: ").strip().split()
num = int(exp[0])
num2 = int(exp[2])

if exp[1] == "/":
    if exp[2] == 0:
        print("You cant divide by 0")
    else:
        print(f"{num / num2:.1f}")
elif exp[1] == "+":
    print(f"{num + num2:.1f}")
elif exp[1] == "-":
    print(f"{num - num2:.1f}")
elif exp[1] == "*":
    print(f"{num * num2:.1f}")
else:
    print("wrong operator")
