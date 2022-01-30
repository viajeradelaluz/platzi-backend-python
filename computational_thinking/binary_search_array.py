#!/usr/bin/python3
"""Binary Search

Finds a number by binary search.
    """

import time


def binary_search_array(number, array):
    """ Binay search with an array as search place """

    low = 0
    high = len(array) - 1
    num_iterations = 0

    start = time.time()

    while low <= high:
        middle = (low + high) // 2
        print(f"{array[low]} ... {array[middle]} ... {array[high]}")

        if array[middle] == number:
            answer = "is"
            break
        if number < array[middle]:
            high = middle - 1
        else:
            low = middle + 1

        num_iterations += 1
        answer = "is not"

    end = time.time()
    final_time = end - start

    print(f"Low ... Middle ... High\n")
    print(f"{number} {answer} on the list.")
    print(f"{num_iterations} iterations were done in {final_time} seconds.")


NUMBER = int(input("Enter a number: "))

print("Create the list of numbers to search through. "
      f"For example: [2 4 6 10 -5 12 {NUMBER}]")

ARRAY = list(map(int, input("Enter the elements separated by space.\n"
                            ">> ").strip().split()))
ARRAY = list(set(ARRAY))
ARRAY.sort()

print(f"\n{ARRAY}")

binary_search_array(NUMBER, ARRAY)
