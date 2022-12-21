#!/usr/bin/python3
import math
"""
Module that writes class MagicClass to emulate
Python bytecode

"""


class MagicClass:
    """Magic class

    Emulatyes python bytecode

    """
    def __init__(self, radius=0):
        """init

        getting the radius

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Area

        calculates the area

        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Circumference

        Calculates the circumference

        """
        return (2 * math.pi) * self.__radius
