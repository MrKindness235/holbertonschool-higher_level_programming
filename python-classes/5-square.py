#!/usr/bin/python3
"""Now Square will be able to check if the size it is given is right."""


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

    def my_print(self):
        """This prints the Square. Is this self-reflection?"""
        if self.__size == 0:
            print("")
        for row in range(self.__size):
            for column in range(self.__size):
                print("#", end="")
            print("")
