#!/usr/bin/python3
"""A new step for the Rectangle class."""


class Rectangle:
    """It's a formful rectangle."""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width and self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        for row in range(self.__height):
            for col in range(self.__width):
                print("#", end="")
            print("")
        return ""
