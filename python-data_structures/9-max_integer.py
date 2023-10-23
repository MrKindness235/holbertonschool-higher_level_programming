#!/usr/bin/python3
def max_integer(my_list=[]):
    """Sorts given list and returns highest Value."""
    if not my_list:
        return None
    new_list = sorted(my_list, reverse=True)
    return new_list[0]
