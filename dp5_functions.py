def main():
    year = int(input("What's Year? "))
    leap = is_leap_year(year)
    print(leap)


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return "{} is a leap year".format(year)
    elif year % 400 == 0:
        return "{} is a leap year".format(year)
    else:
        return "{} is not a leap year".format(year)


if __name__ == "__main__":
    main()
