#!/usr/bin/python3
"""Exhaustive Enumeration

Module to try all the numerical possibilities to find
the square root of a number.
    """

import time


def square_root(number):
    """ Finds the square root, number by number """

    root = 0
    num_iterations = 0

    start = time.time()

    while root**2 < number:
        print(f"{root} ", end="")
        root += 1
        num_iterations += 1

    end = time.time()
    final_time = round(end - start, 4)
    print("\nNumbers squared until find the answer.\n")

    if root**2 == number:
        print(f"The square root of {number} is {root}.")
    else:
        print(f"{number} doesn't have an integer square root.")

    print(f"{num_iterations} iterations were done in {final_time} seconds.")


NUMBER = int(input("Enter a number: "))
square_root(NUMBER)
