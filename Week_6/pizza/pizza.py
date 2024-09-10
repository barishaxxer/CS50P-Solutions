import sys
from tabulate import tabulate
import csv


def main():

    if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
        sys.exit("Invalid arguments.")

    holder = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                holder.append(row)

            # headers olarak fieldnames kullanılıyor
            print(tabulate(holder, headers=reader.fieldnames, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("file not found")


main()
