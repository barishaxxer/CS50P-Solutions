months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}
while True:
    prompted = input("Date: ")
    try:
        m, d, y = prompted.strip().split("/")
        if int(m) > 12 or 0 >= int(m) or int(d) > 31 or 0 > int(d):
            continue
        else:
            print(f"{y}-{int(m):02d}-{int(d):02d}")
            break

    except ValueError:
        try:
            md, y = prompted.split(",")
            m, d = md.split()
            if m not in months or int(d) > 31 or 0 >= int(d):
                continue
            else:
                m = months.get(m)
                print(f"{y}-{m:02d}-{int(d):02d}")
                break
        except ValueError:
            pass
