def main():
    data = input("what time is it: ")
    comp = convert(data)
    if 7<= comp <= 8:
        print("breakfast time")
    elif 12<= comp <= 13:
        print("lunch time")
    elif 18<= comp <= 19:
        print("dinner time")
    else:
        pass
def convert(time):
    fhour = None
    fmin = None
    if time.endswith("a.m.") or time.endswith("p.m."):
        hmin,sup = time.split()
        hour,min = hmin.split(":")
        fmin = float(min) / 60
        if "p.m." in time and hour < 12:
            fhour = 12 + float(hour)
        else:
            fhour = float(hour)

    else:
        hour2,min2 = time.split(":")
        fhour = float(hour2)
        fmin = float(min2) /60

    return fhour + fmin

if __name__ == "__main__":
    main()
