import datetime
import inflect
import sys
import re


class Time:

    @staticmethod
    def convert(start):
        if not len(start.split("-")) == 3:
            sys.exit("Invalid time format.")
        time_since = (
            datetime.date.today() - datetime.datetime.strptime(start, "%Y-%m-%d").date()
        )
        i = inflect.engine()
        final_time = f"{i.number_to_words(time_since.days * 24 * 60).capitalize().replace(",", "")} minutes"
        and_accurate = re.sub(r"\b and\b", "", final_time)
        replaced = re.sub(r"\bthousand\b", "thousand,", and_accurate)
        final_replaced = re.sub(r"\bmillion\b", "million,", replaced)
        return final_replaced


def main():
    birth_date = input("Date of Birth: ")

    print(Time.convert(birth_date))


if __name__ == "__main__":
    main()
