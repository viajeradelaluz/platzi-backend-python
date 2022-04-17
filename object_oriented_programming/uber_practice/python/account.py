#!/usr/bin/python3
""" Practice of declaring classes and objects in Python.
    This module is for superclass Account.
    """


class Account:
    id = int
    name = str
    document = str
    email = str
    password = str

    # __init__ is the magic method to declare constructors
    def __init__(self, name, document):
        self.name = name
        self.document = document
