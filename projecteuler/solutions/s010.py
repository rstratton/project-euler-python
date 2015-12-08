#!/usr/bin/env python3

"""
PROBLEM: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.  Find the sum of
all the primes below two million.
"""


from projecteuler.numbers import primes
from itertools import takewhile


def solve():
    return sum(takewhile(lambda x: x < 2000000, primes))


if __name__ == "__main__":
    print(solve())
