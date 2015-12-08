#!/usr/bin/env python3

"""
PROBLEM: A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99.  Find the
largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

def is_palindromic_num(n):
    # Numbers ending in "0" can't be palindromes
    return n % 10 != 0 and is_palindrome(str(n))

def solve():
    return max(n * m for n in range(100, 1000)
                     for m in range(n,   1000)
                     if is_palindromic_num(n * m))


if __name__ == "__main__":
    print(solve())
