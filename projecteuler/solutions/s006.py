#!/usr/bin/env python3

"""
PROBLEM: Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def solve():
    return (sum(range(1, 101)) ** 2) - sum(n*n for n in range(1, 101))


if __name__ == "__main__":
    print(solve())
