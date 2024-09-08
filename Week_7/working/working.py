import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.match(r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", s)
    if not match:
        raise ValueError("Invalid input format")

    f_hour, f_min, f_form, l_hour, l_min, l_form = match.groups()
    f_min = int(f_min or 0)
    l_min = int(l_min or 0)
    f_hour = int(f_hour) % 12 + (12 if f_form == "PM" else 0)
    l_hour = int(l_hour) % 12 + (12 if l_form == "PM" else 0)

    if not (0 <= f_hour <= 23 and 0 <= f_min <= 59 and 0 <= l_hour <= 23 and 0 <= l_min <= 59):
        raise ValueError("Invalid time format")

    return f"{f_hour:02d}:{f_min:02d} to {l_hour:02d}:{l_min:02d}"

if __name__ == "__main__":
    main()
