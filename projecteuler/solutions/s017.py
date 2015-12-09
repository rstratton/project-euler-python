#!/usr/bin/env python3

"""
PROBLEM: If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the
numbers from 1 to 1000 (one thousand) inclusive were written out in words, how
many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""


def digit_to_s(d):
    return {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }[d]

def thousands_to_s(n):
    s = digit_to_s((n % 10000) // 1000)
    if s != "":
        return s + "thousand"
    else:
        return ""

def hundreds_to_s(n):
    s = digit_to_s((n % 1000) // 100)
    if s != "":
        return s + "hundred"
    else:
        return ""

def tens_and_ones_to_s(n):
    if len(str(n)) > 1:
        tens, ones = (n % 100) // 10, (n % 10)
        if tens == 1:
            return {
                10: "ten",
                11: "eleven",
                12: "twelve",
                13: "thirteen",
                14: "fourteen",
                15: "fifteen",
                16: "sixteen",
                17: "seventeen",
                18: "eighteen",
                19: "nineteen"
            }[tens * 10 + ones]
        else:
            return {
                0: "",
                2: "twenty",
                3: "thirty",
                4: "forty",
                5: "fifty",
                6: "sixty",
                7: "seventy",
                8: "eighty",
                9: "ninety"
            }[tens] + digit_to_s(ones)
    else:
        return digit_to_s(n)

def number_to_s(n):
    thousands = thousands_to_s(n)
    hundreds = hundreds_to_s(n)
    tens_and_ones = tens_and_ones_to_s(n)
    if hundreds != "" and tens_and_ones != "":
        return "".join([thousands, hundreds, "and", tens_and_ones])
    else:
        return "".join([thousands, hundreds, tens_and_ones])

def solve():
    return sum(len(number_to_s(n)) for n in range(1, 1001))


if __name__ == "__main__":
    print(solve())
