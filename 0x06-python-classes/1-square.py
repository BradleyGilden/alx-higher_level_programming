#!/usr/bin/python3

"""
This module contains a Square class

Author: Bradley Dillion Gilden
Date: 27-06-2023
"""


class Square:
    """Square initialises an instance attribute
    Attributes(instance):
        @private
        size(int): stores the size of an object of Square
    """
    def __init__(self, size):
        """__init__ - constructor
        Args:
            size(int): size of square
        """
        self.__size = size
