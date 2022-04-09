#!/usr/bin/python3
""" Detects whether a number is prime or not and
    gets the list of the number dividers.
    """


def divisibility_test(n):
    LIMIT = n / 2
    base = 1
    dividers = []

    while base <= LIMIT:
        if n % base == 0:
            dividers.append(base)
        base += 1
    dividers.append(n)

    return dividers


def prime_number(n):
    if n == 1:
        print(f"--> {n} is not a prime number.")
        return

    dividers = divisibility_test(n)
    if len(dividers) == 2:
        print(f"{dividers}\n"
              f"--> {n} is a prime number.")
    else:
        print(f"{dividers}\n"
              f"--> {n} is not a prime number.")


# Entry point
if __name__ == "__main__":
    number = int(input("""
    +-+-+-+-+--+-+-+-+--+-+
··· |P|R|I|M|  |N|U|M|  |R| (?) ···
    +-+-+-+-+  +-+-+-+  +-+
             x        xx
             x        .x     
             .        ..

Enter a number: """))

    prime_number(number)
