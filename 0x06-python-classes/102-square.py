#!/usr/bin/python3
"""102-square

This module writes a class square based
on 4-square.py

"""


class Square:
    """Class square

    defines a square by size:

        size must be an integer
        size must not be negative

    """
    def __init__(self, size=0):
        """initialize square objects

        Sets size equal to 0 by default
        Checks if size has the correct type and value

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Property size

        gets the value of __size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter

        sets the value of __size

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Area

        Returns the area of a square

        """
        return self.__size ** 2

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
