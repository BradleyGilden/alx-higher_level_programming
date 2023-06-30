#!/usr/bin/python3

"""
This module contains print_square which prints a square of #

Author: Bradley Dillion Gilden
Date: 29-06-2023
"""


def print_square(size):
    """prints a square of '#', of size: size * size

    Args:
        size: size of square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
