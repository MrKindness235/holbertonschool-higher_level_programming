#!/usr/bin/python3
def max_integer(my_list=[]):
    """Sorts given list and returns highest Value."""
    new_list = sorted(my_list, reverse=True)

    return new_list[0]
