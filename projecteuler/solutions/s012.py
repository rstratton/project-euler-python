#!/usr/bin/env python3

"""
PROBLEM: The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The
first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors. What
is the value of the first triangle number to have over five hundred divisors?
"""


from projecteuler.util import divisors
from projecteuler.util import prime_factors
from itertools import count


def tri_nums():
    """
    Yield the sequence of triangle numbers starting with 1
    """
    current_num = 0
    for n in count(1):
        current_num += n
        yield current_num

def solve():
    for tri_num in tri_nums():
        if len(divisors(tri_num)) > 500:
            return tri_num


if __name__ == "__main__":
    print(solve())
