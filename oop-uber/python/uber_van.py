#!/usr/bin/python3
""" UberVan is a subclass of Car class
    """

from car import Car


class UberVan (Car):
    type_car_accepted = list
    seat_material = list

    # UberVan constructor should hava a least the same parameters
    # of its superclass Car, then use 'super' to call them.
    def __init__(self, license, driver, type_car_accepted, seat_material):
        super().__init__(license, driver)
        self.type_car_accepted = type_car_accepted
        self.seat_material = seat_material
