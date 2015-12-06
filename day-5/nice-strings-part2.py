#!/usr/bin/env python

import re

"""
Now, a nice string is one with all of the following properties:
It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
"""

def is_nice_string(string_in_question):
    two_letters_twice = re.match( r'.*([a-z][a-z]).*\1.*', string_in_question)
    if not two_letters_twice:
        return False

    one_letter_sandwich = re.match( r'.*([a-z])[a-z]{1}\1.*', string_in_question)
    if not one_letter_sandwich:
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

def tests():
    if not is_nice_string("qjhvhtzxzqqjkmpb"):
        print "qjhvhtzxzqqjkmpb should be nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz)."

    if not is_nice_string("xxyxx"):
        print "xxyxx should be nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap."

    if is_nice_string("uurcxstgmygtbstg"):
        print "uurcxstgmygtbstg should not be nice because it has a pair (tg) but no repeat with a single letter between them."

    if is_nice_string("ieodomkazucvgmuy"):
        print "ieodomkazucvgmuy should not be nice because it has a repeating letter with one between (odo), but no pair that appears twice."

main()