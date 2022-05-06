#!/usr/bin/python3
"""Approximation Algorithm

Try all the numerical possibilities to find
the square root of a number.
    """

import time


def square_root_aproximation(number):
    """ Find the root by aproximation / epsilon """

    root = 0
    epsilon = 0.01
    iterations = epsilon**2
    num_iterations = 0

    start = time.time()

    while abs(root**2 - number) >= epsilon and root <= number:
        print(f"{abs(round(root**2 - number, 6))} ... {round(root, 6)}")
        root += iterations
        num_iterations += 1

    end = time.time()
    final_time = round(end - start, 5)

    print("Number to zero ... Closest root\n")
    if abs(root**2 - number) >= epsilon:
        print(f"Square root of {number} not found.")
    else:
        print(f"Square root of {number} is {round(root, 5)}.")

    print(f"{num_iterations} iterations were done in {final_time} seconds.")


NUMBER = int(input("Enter a number: "))
square_root_aproximation(NUMBER)
