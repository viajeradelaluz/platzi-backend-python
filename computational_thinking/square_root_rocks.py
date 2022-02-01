"""Square Root Rocks!

Program with three methods to get the square root of a number.
"""


def square_root_binary_search(number):
    """ Binary search for the square root """
    epsilon = 0.0001
    low = 0.00
    high = max(1, number)
    middle = (low + high) / 2

    while abs(middle**2 - number) >= epsilon:
        if middle**2 < number:
            low = middle
        else:
            high = middle
        middle = (low + high) / 2

    print(f"Square root of {number} is {round(middle, 4)}")


def square_root_aproximation(number):
    """ Finds the root by aproximation / epsilon """
    root = 0
    epsilon = 0.01
    iterations = epsilon**2

    while abs(root**2 - number) >= epsilon and root <= number:
        root += iterations
    if abs(root**2 - number) >= epsilon:
        print(f"Square root of {number} not found.")
    else:
        print(f"Square root of {number} is {round(root, 5)}.")


def square_root_exhaustive_numeration(number):
    """ Finds the square root, number by number """
    root = 0
    while root**2 < number:
        root += 1
    if root**2 == number:
        print(f"Square root of {number} is {root}.")
    else:
        print(f"{number} doesn't have an integer square root.")


print()
greeting = "Welcome to Square Root Rocks!"
print(greeting.center(45, "·"))
NUMBER = int(input("\nEnter a number to get the square root: "))
get_method = int(input("""Select the method:
    [1] - Exhaustive enumeration
    [2] - Aproximation
    [3] - Binary search
>> """))

if get_method == 1:
    square_root_exhaustive_numeration(NUMBER)
elif get_method == 2:
    square_root_aproximation(NUMBER)
else:
    square_root_binary_search(NUMBER)
