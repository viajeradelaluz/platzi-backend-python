#!/usr/bin/python3
"""Binary Search

Finds the square root of a number by binary search.
    """

import time


def square_root_binary_search_no_array(number):
    """ Binay search without array """

    epsilon = 0.0001
    low = 0.00
    high = max(1, number)
    middle = (low + high) / 2
    num_iterations = 0

    start = time.time()

    while abs(middle**2 - number) >= epsilon:
        print(f"{round(low, 3)} ... {round(middle, 3)} "
              f"[{round(middle**2, 3)} - {number} = "
              f"{abs(round(middle**2 - number, 3))}] ... "
              f"{round(high, 3)}")

        if middle**2 < number:
            low = middle
        else:
            high = middle

        middle = (low + high) / 2
        num_iterations += 1

    end = time.time()
    final_time = round(end - start, 5)

    print(f"Low ... Middle [Middle squared - number] ... High\n")
    print(f"Square root of {number} is {round(middle, 4)}")
    print(f"{num_iterations} iterations were done in {final_time} seconds.")


NUMBER = int(input("Enter a number: "))
square_root_binary_search_no_array(NUMBER)
