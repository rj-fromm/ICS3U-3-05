#!user/bin/env python3

# Created by: RJ Fromm
# Created on: October 2019
# This program determines what month corresponds to numbers from 1-12


def main():

    month = int(input("Please enter a number from 1-12 : "))

    if month == 1:
        print("january")

    elif month == 2:
        print("Febuary")

    elif month == 3:
        print("March")

    elif month == 4:
        print("April")

    elif month == 5:
        print("May")

    elif month == 6:
        print("June")

    elif month == 7:
        print("July")

    elif month == 8:
        print("August")

    elif month == 9:
        print("September")

    elif month == 10:
        print("October")

    elif month == 11:
        print("November")

    elif month == 12:
        print("December")

    else:
        print("Invalid number")


if __name__ == "__main__":
    main()
