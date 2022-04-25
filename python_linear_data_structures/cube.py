#!/usr/bin/python3
"""
Module to create 3D arrays.
Methods:
    - Get height
    - Get width
    - Get x
    - Items access
    - Set random items on the array
    - String representation
"""

import random
from array_module import Array


class Cube():
    def __init__(self, x, y, z, fill_value=None):
        self.data = Array(x)
        for row in range(x):
            self.data[row] = Array(y)
            for col in range(y):
                self.data[row][col] = Array(z, fill_value)

    def height(self):
        return len(self.data)

    def width(self):
        return len(self.data[0])

    def deep(self):
        return len(self.data[0][0])

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, x, y, z, value):
        self.data[x][y][z] = value

    def __iter__(self):
        self.data = [[[random.randint(1, 20) for _ in range(self.deep())]
                      for _ in range(self.width())] for _ in range(self.height())]

    def __str__(self):
        cube = '3D array = [\n'
        for x in range(self.height()):
            cube += '\t[\n'
            for y in range(self.width()):
                deep = [self.data[x][y][z] for z in range(self.deep())]
                cube += f'\t\t{deep}\n'
            cube += '\t]\n'
        cube += ']'
        return cube


if __name__ == '__main__':
    c = Cube(2, 3, 4)
    c.__iter__()
    print(c)
