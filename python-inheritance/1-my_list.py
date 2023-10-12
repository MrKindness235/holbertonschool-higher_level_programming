#!/usr/bin/python3
"""This is Mylist. A list that I have claimed."""


class MyList(list):
    """Indeed, mine and only mine."""

    def print_sorted(self):
        print("{}".format(sorted(self)))
