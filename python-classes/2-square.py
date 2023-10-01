#!/usr/bin/python3
"""Now Square will be able to check if the size it is given is right."""


class Square:
    """Defines the Square's size correctly."""
    def __init__(self, size=0):
        if size is not int:
            raise TypeError("size must be an intger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
