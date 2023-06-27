#!/usr/bin/python3

"""
converting bytcode to python code

Author: Bradley Dillion Gilden
Date: 27-06-2023
"""

import math


class MagicClass:
    """Computes properties of a Circle"""

    def __init__(self, radius=0):
        """__init__ - Initialize a MagicClass.
        Arg:
            radius (int): The radius of a new MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference"""
        return (2 * math.pi * self.__radius)
