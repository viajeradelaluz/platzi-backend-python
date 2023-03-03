# Drunkard Simulation

## Simulation Specifics

## Models

- A `Drunkard` main class representing a drunk person that can move in a 2D plane.
- A `NormalDrunkard` class that moves the drunkard in a random walk distribution: one step to the right, left, up, down, up-right, up-left, down-right or down-left.
- A `HipsterDrunkard` class that moves the drunkard in a random walk distribution: one step to the right, left, up, down, up-right, up-left, down-right or down-left, but with a 10% chance of moving two steps in the same direction.
- A `Coordinate` class representing a point in a 2D plane.
- A `Plane2D` class representing a 2D plane.

## Views

- Prompt for the number of steps the drunkard will take.
- Prompt for the number of simulations to run.
- Prompt for the drunkard type: normal or hipster.
- Display the drunkard's statistics: average distance, maximum distance, minimum distance.
- Display a graph with all the drunkard's positions.

## Controller

- Start the simulation: `WalkSimulation` class expecting the number of steps, the number of simulations and the drunkard type.
- Assign the drunkard name and the coordinates of his starting position on the plane.
- Create a plane for each simulation and assign the drunkard to it.
- Move the drunkard in the plane for the number of steps.
- Store the coordinates of the positions the drunkard had walked.
