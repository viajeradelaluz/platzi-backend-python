"""
Main module.
"""

from models import NormalDrunken, Coordinate, Space


def go_hike(space: Space, drunken: NormalDrunken, steps: int) -> float:
    """ """
    origin = space.get_coordinate(drunken)

    for _ in range(steps):
        space.move_drunken_man(drunken)

    destination = space.get_coordinate(drunken)
    return origin.distance(destination)


def walk_simulation(steps: int, n_simulations: int, drunken_class) -> None:
    """ """
    drunken = drunken_class(name="Bacchus")
    start_position = Coordinate(0, 0)
    distances = []

    for _ in range(n_simulations):
        space = Space()
        space.add_drunken_man(drunken, start_position)
        hike = go_hike(space, drunken, steps)
        distances.append(round(hike, 1))

    return distances


def main():
    """ """
    steps = [10, 100, 1000, 10000]
    n_simulations = 100

    for step in steps:
        distances = walk_simulation(step, n_simulations, NormalDrunken)

        # Statistics to print
        avg_distance = round(sum(distances) / len(distances), 4)
        max_distance = max(distances)
        min_distance = min(distances)

        print(
            f"{NormalDrunken.__name__} took a {step}-step walk, with an\
            average distance of {avg_distance} steps, a maximum distance of\
            {max_distance} steps and a minimum distance of {min_distance} steps."
        )


if __name__ == "_main_":
    main()
