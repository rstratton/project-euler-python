#!/usr/bin/env python3

"""
PROBLEM: Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.  For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 × 53 = 49714.  What is the total of all the
name scores in the file?
"""


def load_names():
    with open("./projecteuler/resources/p022.txt") as f:
        return sorted(name[1:-1] for name in f.read().split(","))

def char_score(c):
    return ord(c) - ord('A') + 1

def score(name):
    return sum(char_score(c) for c in name)

def solve():
    return sum((i + 1) * score(name) for i, name in enumerate(load_names()))



if __name__ == "__main__":
    print(solve())
