#!/usr/bin/python3
"""Now Square will be able to check if the size it is given is right."""


class Square:
    """Defines the Square's size correctly."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size and position private values."""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.position
    
    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        
 
    def area(self):
        """This calculates the square's area."""
        return (self.__size ** 2)

    def my_print(self):
        """This prints the Square. Is this self-reflection?"""
        if self.__size == 0:
            print("")
        for row in range(self.__size):
            for column in range(self.__size):
                if self.__position[1] > 0:
                    print("")
                else:
                    print("_", end="")
            for column in range(self.__size): 
                print("#", end="")
            print("")
