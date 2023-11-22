#!/usr/bin/python3
"""This handy dandy function woll return the number of keys in a dictionary."""

def number_keys(a_dictionary):
    count = 0
    for index in range(0, len(a_dictionary)):
        count += 1
    return count
