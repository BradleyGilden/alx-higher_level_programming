#!/usr/bin/python3
"""
This module contains a function for adding integers

Author: Bradley Dillion Gilden
Date: 29-06-2023
"""


def add_integer(a, b=98):
    """returns the sum: a + b, as an integer

    Note: user must atleast assign a value to a
          accepts integer and float arguments
    Raises:
        TypeError - if a or b is not of type int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(a, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
