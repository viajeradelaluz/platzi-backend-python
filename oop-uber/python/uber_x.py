#!/usr/bin/python3
""" UberX is a subclass of Car class
    """

from car import Car


class UberX (Car):
    brand = str
    model = str

    # UberX constructor should hava a least the same parameters
    # of its superclass Car, then use 'super' to call them.
    def __init__(self, license, driver, brand, model):
        super().__init__(license, driver)
        self.brand = brand
        self.model = model
