#!/usr/bin/env python3

"""
PROBLEM: 2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.  What is the smallest positive number that
is evenly divisible by all of the numbers from 1 to 20?
"""


from projecteuler.util import prime_factors
from collections import Counter


def solve():
    factorizations = [prime_factors(n) for n in range(1, 21)]
    factor_tallies = [Counter(list) for list in factorizations]
    unique_factors = set(factor for list in factorizations for factor in list)

    answer_factor_tally = Counter()
    for factor in unique_factors:
        answer_factor_tally[factor] = \
                max(tally[factor] for tally in factor_tallies)

    answer = 1
    for factor, count in answer_factor_tally.items():
        answer *= factor ** count

    return answer


if __name__ == "__main__":
    print(solve())
