#!/usr/bin/python3
""" Practice of declaring classes and objects in Python.
    This module is the entry point of the program.
    """

from account import Account
from car import Car
from uber_x import UberX


if __name__ == '__main__':
    # Instancing objects of Car class
    car = Car('HYF562', Account('Esteban Giraldo', '1002'))
    car.passenger(2)
    car.printDataCar()

    # Instancing objects of UberX class (subclass of Car class)
    uber_x = UberX('LXW573', Account(
        'Agustin Aldana', '1012'), 'Volvo', '2021')
    uber_x.passenger(4)
    uber_x.printDataCar()
