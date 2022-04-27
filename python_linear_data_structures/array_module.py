#!/usr/bin/python3
"""
Module to create restrictive arrays based on list().
Magic methods:
    - Length
    - String representation
    - Get item at index
    - Set item at index
    - Set random items on the array
    - Sum all values of the array
"""

from functools import reduce
import random


class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = [fill_value for _ in range(capacity)]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __iter__(self):
        self.items = list(map(lambda _: random.randint(1, 20), self.items))

    def __sum__(self):
        try:
            return reduce(lambda a, b: a + b, self.items)
        except TypeError:
            print('You can only sum arrays of the same type.')


def main():
    a = Array(2)
    a.__iter__()
    print(a)


if __name__ == '__main__':
    main()
