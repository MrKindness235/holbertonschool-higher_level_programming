#!/usr/bin/python3
"""A new, refined, version of the size value setting method."""


class Square:
    """Defines the Square's size correctly."""
    def __init__(self, size=0):
        """Initializes the size value."""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This calculates the square's area."""
        return (self.__size ** 2)
