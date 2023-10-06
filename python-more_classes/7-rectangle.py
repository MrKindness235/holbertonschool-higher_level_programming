#!/usr/bin/python3
"""A new step for the Rectangle class."""


class Rectangle:
    """It's a formful rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        if self.height and self.width == 0:
            return ""
        wyrm = []
        for row in range(self.__height):
            if row > 0:
                wyrm.append("\n")
            for col in range(self.__width):
                wyrm.append(f"{self.print_symbol}")
        return "".join(wyrm)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area == rect_2.area:
            return rect_1
        if rect_1.area > rect_2.area:
            return rect_1
        if rect_1.area < rect_2.area:
            return rect_2
