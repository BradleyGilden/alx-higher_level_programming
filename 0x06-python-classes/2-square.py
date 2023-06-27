#!/usr/bin/python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 27-06-2023
"""


class Square:
    """Square initialises an instance attribute
    Attributes(instance):
        @private
        size(int): stores the size of an object of Square
    """
    def __init__(self, size=0):
        """__init__ - constructor
        Args:
            size(int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
