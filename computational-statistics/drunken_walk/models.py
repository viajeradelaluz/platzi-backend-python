"""
"""
import random


class DrunkenMan:
    """ """

    def __init__(self, name: str) -> None:
        self.name = name


class NormalDrunken(DrunkenMan):
    """ """

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def walk(self) -> tuple:
        """"""
        # right, left, up, down
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(movements)


class Coordinate:
    """ """

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, delta_x: int, delta_y: int) -> None:
        """ """
        return Coordinate(self.x + delta_x, self.y + delta_y)

    def distance(self, destine) -> None:
        """ """
        delta_x = self.x - destine.x
        delta_y = self.y - destine.y

        # Pythagoras Method
        return (delta_x**2 + delta_y**2) ** 0.5


class Plane2D:
    """ """

    def __init__(self) -> None:
        self.position = {}

    def add_drunken_man(self, drunken_man: NormalDrunken, coordinate: Coordinate):
        self.position[drunken_man] = coordinate

    def move_drunken_man(self, drunken_man):
        delta_x, delta_y = drunken_man.walk()
        drunken_position = self.position[drunken_man]
        destination = drunken_position.move(delta_x, delta_y)

        self.position[drunken_man] = destination

    def get_coordinate(self, drunken_man: NormalDrunken) -> Coordinate:
        """ """
        return self.position[drunken_man]
