#!/usr/bin/env python3

"""
PROBLEM: What is the largest prime factor of the number 600851475143?
"""


from projecteuler.util import prime_factors_large_n


def solve():
    return max(prime_factors_large_n(600851475143))


if __name__ == "__main__":
    print(solve())
