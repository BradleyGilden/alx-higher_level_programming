#!/usr/bin/python3

"""
This module contains a function for adding integers

Author: Bradley Dillion Gilden
Date: 29-06-2023
"""


def add_integer(a, b=98):
    """ returns the sum: a + b 
    Note: user must atleast assign a value to a
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
