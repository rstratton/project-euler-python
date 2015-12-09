#!/usr/bin/env python3

"""
PROBLEM: Starting in the top left corner of a 2x2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom right
corner. How many such routes are there through a 20x20 grid?
"""


from projecteuler.util import memoize


@memoize
def num_paths(i, j):
    if i == 0 or j == 0:
        return 1
    else:
        return num_paths(i - 1, j) + num_paths(i, j - 1)

def solve():
    """
    The value of '40 choose 20' also yields the answer to this problem.
    """
    return num_paths(20, 20)


if __name__ == "__main__":
    print(solve())
