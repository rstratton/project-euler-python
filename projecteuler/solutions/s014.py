#!/usr/bin/env python3

"""
PROBLEM: The following iterative sequence is defined for the set of positive
integers:

    n → n/2    (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.  Which starting number, under one
million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


from projecteuler.util import memoize


def collatz_step(n):
    """
    Return the next number in the Collatz sequence after 'n'.
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

@memoize
def collatz_len(n):
    """
    Return the number of terms in the Collatz sequence which starts with 'n'
    """
    if n == 1:
        return 1
    else:
        return 1 + collatz_len(collatz_step(n))


def solve():
    return max((collatz_len(n), n) for n in range(1, 1000000))[1]


if __name__ == "__main__":
    print(solve())
