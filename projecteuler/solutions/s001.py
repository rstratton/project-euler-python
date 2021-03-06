#!/usr/bin/env python3

"""
PROBLEM: Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solve():
    return sum([n for n in range(1,1000) if n % 3 == 0 or n % 5 == 0])


if __name__ == "__main__":
    print(solve())
