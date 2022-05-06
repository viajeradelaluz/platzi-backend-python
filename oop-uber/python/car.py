#!/usr/bin/python3
""" Practice of declaring classes and objects in Python.
    This module is for superclass Car.
    """

from account import Account


class Car:
    id = int
    license = str
    driver = Account("", "")
    __passenger = int  # class private variable = restricted

    # __init__ is the magic method to declare constructors
    def __init__(self, license, driver):
        self.license = license
        self.driver = driver

    # Getter
    # We don't use @property, because that's speacially for instances variables
    # (private or public) like 'self.license' and 'self.driver'
    def passenger(self):
        return self.__passenger

    # Setter
    # We don't use @passenger.setter, because that's speacially for instances
    # variables (private or public) like 'self.license' and 'self.driver'
    def passenger(self, value):
        if value >= 4:
            self.__passenger = value
        else:
            self.__passenger = None
            print("Value Error: All cars should have at least 4 passengers.")

    def printDataCar(self):
        if self.__passenger is not None:
            print(f"License: {self.license} - "
                  f"Driver Name: {self.driver.name} - Passengers: {self.__passenger}")
