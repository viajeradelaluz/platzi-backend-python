# Computational Statistics with Python

## Learning Objectives

- Learn when to use dinamic programming and its benefits.
- Understand the difference between deterministic and stochastic algorithms.
- Learn how to use stochastic algorithms to solve problems.
- Create computational simulations to solve problems.

## Dinamic Programming

Technique to optimize the performance of certain types of problems. It is based on the idea of dividing the problem into smaller subproblems and solving them in a recursive way. The solution to the subproblems is stored in a dictionary (memoization), so that when a subproblem is solved, it is not necessary to solve it again.

### Memoization

- Stores previously computed values to avoid computing them again.
- Normally, the values are stored in a dictionary, where the queries can be made in constant time O(1).
- Interchanges time for space.
