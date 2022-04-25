#!/usr/bin/python3
"""
Module to create 2D arrays.
Methods:
    - Get height
    - Get width
    - Items access
    - Set random items on the array
    - String representation
"""

import random
from array_module import Array


class Grid():
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def height(self):
        return len(self.data)

    def width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        for row in range(self.height()):
            for col in range(self.width()):
                self.data[row][col] = random.randint(1, 20)

    def __str__(self):
        grid = '2D array = [\n'
        for row in range(self.height()):
            width = []
            for col in range(self.width()):
                width.append(self.data[row][col])
            grid += f'\t{width}\n'
        grid += ']'
        return grid


if __name__ == '__main__':
    g = Grid(3, 5)
    g.__iter__()
    print(g)
