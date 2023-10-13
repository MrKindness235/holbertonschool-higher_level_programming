#!/usr/bin/python3
"""Working in a more refined Rectangle class."""


from .base import Base


class Rectangle(Base):
    """The new Revtangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """In a beginning I giveth width to the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width's very own setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """And then I spoketh: There shalt be height. And height there was."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height very own setter too."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Then this little prick came around."""
        return self.__x

    @x.setter
    def x(self, value):
        """The only reason I gave this a setter is because I was obligated."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """And then it cameth to thyself! The question to thy answer!"""
        return self.__y

    @y.setter
    def y(self, value):
        """I wasn't goin to. But then I asked myself, Why not?"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
