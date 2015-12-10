from itertools import chain
from itertools import combinations
from functools import reduce
from operator import mul
import functools

class _Primes(object):

    def __init__(self):
        """
        Discover all primes from 0 to 'limit' and save the results in
        'self.primes_list' and 'self.primes_set'
        """
        self.primes_list, self.limit = [2, 3, 5, 7], 10
        self.primes_set = set(self.primes_list)

    def _expand(self):
        new_limit = int(self.limit * 2)
        sieve = _Sieve(self.limit, new_limit, self.primes_list)
        self.primes_list.extend(sieve.primes)
        self.primes_set.update(sieve.primes)
        self.limit = new_limit

    def __contains__(self, n):
        while n >= self.limit:
            self._expand()
        return n in self.primes_set

    def __getitem__(self, key):
        while key >= len(self.primes_list):
            self._expand()
        return self.primes_list[key]

    def __iter__(self):
        return _PrimesIter(self)


class _PrimesIter(object):
    def __init__(self, primes):
        self.primes, self.i = primes, 0

    def __iter__(self):
        return self

    def __next__(self):
        prime = self.primes[self.i]
        self.i += 1
        return prime


class _Sieve(object):
    def __init__(self, start, end, known_primes):
        self.start, self.end, self.primes = start, end, []
        self._sieve = [True] * (end - start)
        self._find_primes(known_primes)

    def _find_primes(self, known_primes):
        for prime in known_primes:
            self._eliminate_multiples(prime)
        for i in range(len(self._sieve)):
            if self._sieve[i]:
                self.primes.append(self.start + i)
                self._eliminate_multiples(self.start + i)

    def _eliminate_multiples(self, n):
        first_multiplier = max(2, ((self.start - 1) // n) + 1)
        for multiple in range(first_multiplier * n, self.end, n):
            self._sieve[multiple - self.start] = False


# Instantiate publicly-available instance of _Primes
primes = _Primes()


def prime_factors(n):
    """
    Return a list containing the prime factors of 'n'

    """
    factors = []
    if n in [0, 1]:
        return []
    for p in primes:
        if n % p == 0:
            factors.append(p)
            break
    factors.extend(prime_factors(n / p))
    return factors


def powerset(iterable):
    """
    Taken from: https://docs.python.org/3.1/library/itertools.html
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def product(iterable):
    """
    Return the multiplicative product of a sequence of numbers.
    """
    return reduce(mul, iterable, 1)


def divisors(n):
    """
    Return a set of all the divisors of n (including 1 and n).
    """
    return set(product(factors) for factors in powerset(prime_factors(n)))


def memoize(obj):
    """
    Taken from: https://wiki.python.org/moin/PythonDecoratorLibrary
    """
    cache = obj.cache = {}
    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer


def flatten(list_of_lists):
    """
    Taken from: https://docs.python.org/3.1/library/itertools.html
    Flatten one level of nesting in a list of lists
    """
    return chain.from_iterable(list_of_lists)
