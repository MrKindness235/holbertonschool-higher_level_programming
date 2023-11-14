#!/usr/bin/python3
"""This is Mylist. A list that I have claimed as mine."""


class MyList(list):
    """Indeed, mine and only mine."""

    def print_sorted(self):
        print("{}".format(sorted(self)))
