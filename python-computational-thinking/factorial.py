"""Factorial

Module to get the factorial of a number.
Formula: n! = n x (n - 1)!

Example:
5! = 5 x (4)! ...
    """

import sys  # To know the recursion limit on Python


def factorial(n):
    """ Gets the factorial of n recursively """

    formula = f"{n} x "

    if n == 1:
        print(f"{formula[:-3]}")
        return 1
    print(f"{formula}", end="")
    return n * factorial(n - 1)


def recursion_limit(limit):
    """ Knowing the recursion limit on Python """

    std_limit = sys.getrecursionlimit()
    print(f"---\nStandard recursion limit in Python: {std_limit}")

    sys.setrecursionlimit(limit)
    new_limit = sys.getrecursionlimit()
    print(f"New recursion limit: {new_limit}\n")


NUMBER = int(input("\nEnter a number: "))
print(f"Factorial number: {factorial(NUMBER)}")
recursion_limit(250)
