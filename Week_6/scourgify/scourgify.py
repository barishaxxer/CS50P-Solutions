import sys
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Invalid arguments.")
    holder = {}
    try:
        with open(sys.argv[1]) as csvfile:

            reader = csv.DictReader(csvfile)
            with open(sys.argv[2], "w") as newfile:
                writer = csv.DictWriter(newfile, fieldnames=["first", "last", "house"])

                writer.writeheader()
                for row in reader:
                    holder["last"], holder["first"] = (
                        row["name"].replace(" ", "").split(",")
                    )
                    holder["house"] = row["house"]

                    writer.writerow(holder)

    except FileNotFoundError:
        sys.exit("Invalid file.")


main()
