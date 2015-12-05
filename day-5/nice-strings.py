#!/usr/bin/env python

import re

"""
A nice string is one with all of the following properties:
It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
"""

def is_nice_string(string_in_question):
    bad_couples = re.match( r'.*ab|cd|pq|xy.*', string_in_question)
    if bad_couples:
        return False

    num_vowels = re.findall( r'[aeiou]', string_in_question)
    if len(num_vowels) < 3:
        return False

    double_letter = re.match( r'.*([a-z])\1.*', string_in_question)
    if double_letter is not None:
        return False

    return True

def main():
    num_nice_strings = 0

    f = open("input.txt", "r")
    for line in iter(f):
        if is_nice_string(line):
            num_nice_strings += 1
    f.close()

    print "Number of nice strings: " + str(num_nice_strings)

main()
