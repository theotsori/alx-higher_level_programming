#!/usr/bin/python3
import math
"""A class that does exactly as provide bytecode"""


class MagicClass:
    """Definition of a MagicClass"""

    def __init__(self, radius):
        """Initialization of radius"""

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """finding area of the radius"""

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Circumference of the radius"""
        return 2 * math.pi * self.__radius
