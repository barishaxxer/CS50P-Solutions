def main():
    while True:
        fr = input("Fraction: ").strip()
        perc = percentage(fr)
        if perc is not None:
            if 0 <= perc <= 1:
                print("E")
                break
            elif 99 <= perc <= 100:
                print("F")
                break
            elif 1 < perc < 100:
                print(round(perc), "%", sep="")
                break
        else:
            pass


def percentage(fraction):
    try:
        x, y = fraction.split("/")
        return (int(x) / int(y)) * 100
    except (ZeroDivisionError, ValueError):
        return


main()
