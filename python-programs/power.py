#!/usr/bin/python3
""" Get a list of the power of a number below a limit.
    """


def power_of_number(n):
    LIMIT = 10000**2

    counter = 0
    power = n**counter

    while power <= LIMIT:
        print(f"{n}^{counter} = {power}")
        counter += 1
        power = n**counter


if __name__ == "__main__":
    number = int(input("Enter a number to power: "))
    power_of_number(number)
