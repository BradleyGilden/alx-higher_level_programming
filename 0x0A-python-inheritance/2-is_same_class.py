#!/usr/bin/python3

"""
This module contains is_same_class function

Author: Bradley Dillion Gilden
Date: 10-07-2023
"""


def is_same_class(obj, a_class):
    """Determines if object {obj} is exactly an instance of class {a_class}

    Return:
        True: if {obj} is an instance of {a_class}
        False: otherwise
    """
    return type(obj) == a_class
