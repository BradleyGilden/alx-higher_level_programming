#!/usr/bin/python3

"""
This module contains an inherited class of Rectangle: Square

Author: Bradley Dillion Gilden
Date: 10-07-2023
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class inherits Rectangle class with width and height = size

    Args:
        size(int): size of one of the square objects sides
    """
    def __init__(self, size):
        """constructor for the Square class"""
        super().__init__(size, size)
