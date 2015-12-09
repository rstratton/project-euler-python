#!/usr/bin/env python3

"""
PROBLEM: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.  What is the 10 001st prime number?
"""


from projecteuler.util import primes

def solve():
    return primes[10000]


if __name__ == "__main__":
    print(solve())
