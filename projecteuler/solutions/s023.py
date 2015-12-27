#!/usr/bin/env python2

"""
PROBLEM: A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.  By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""


from projecteuler.util import divisors


LIMIT = 28124


def is_abundant(n):
    return sum(divisors(n)) > 2 * n


def abundant_nums(limit=LIMIT):
    """
    Return the list of abundant numbers less than 'limit'
    """
    ab_nums = set()
    for i in range(1, limit):
        if i not in ab_nums and is_abundant(i):
            # Every multiple of an abundant number is abundant
            ab_nums.update(set(range(i, limit, i)))
    return sorted(ab_nums)


def abundant_sums(limit=LIMIT):
    """
    Return the set of sums of abundant numbers less than 'limit'
    """
    ab_nums = abundant_nums(limit)
    sums = set()
    for i, n1 in enumerate(ab_nums):
        for _, n2 in enumerate(ab_nums[i:]):
            if n1 + n2 > limit:
                break
            else:
                sums.add(n1 + n2)
    return sums


def solve():
    return sum(set(range(1, LIMIT)) - abundant_sums())


if __name__ == "__main__":
    print(solve())
