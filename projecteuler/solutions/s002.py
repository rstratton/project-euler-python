#!/usr/bin/env python3

"""
PROBLEM: By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""


from itertools import takewhile


def fibs():
    cur, prev = 1, 0
    while True:
        yield cur
        cur, prev = cur + prev, cur

def solve():
    fibs_leq_4_million = takewhile(lambda x: x <= 4000000, fibs())
    return sum(fib for fib in fibs_leq_4_million if fib % 2 == 0)


if __name__ == "__main__":
    print(solve())
