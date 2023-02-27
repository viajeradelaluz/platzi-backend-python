"""Fibonacci

Module to get the Fibonacci Sequence of a number.

Example:
    1--> 1
    2--> 1, 1 [1+1=2]
    3--> 1, 1, 2 [1+2=3]
    4--> 1, 1, 2, 3 [2+3=5]
    5--> 1, 1, 2, 3, 5 [3+5=8]
    6--> 1, 1, 2, 3, 5, 8 [5+8=13]
    7--> 1, 1, 2, 3, 5, 8, 13 [8+13=21]
    ...
"""

# Save the vale of each fibonacci() call.
# This technique accelerates the calculation time
memoization = {}


def fibonacci(n):
    """ Returns the n Fibonacci Sequence """
    try:
        # Check if n is an integer
        if not isinstance(n, int):
            if not n.isdigit():
                raise TypeError
            n = int(n)

        # Check if n is store in memoization
        if n in memoization:
            return memoization[n]

        # Performance the Fibonacci sequence
        value = 0
        if n == 1 or n == 2:
            value = 1
        if n > 2:
            value = fibonacci(n - 1) + fibonacci(n - 2)

        # Print the sequence
        print(f"{2 if n==1 else n and 1 if n==2 else n}--> {value}")

        memoization[n] = value
        return value

    except TypeError:
        print("The number must be a positive integer")
    except ValueError:
        print("The number must be a positive integer")


NUMBER = input("\nEnter a number: ")
fibonacci(NUMBER)
