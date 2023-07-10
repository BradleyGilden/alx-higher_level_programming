#!/usr/bin/python3

"""
This module contains is_kind_of_class function

Author: Bradley Dillion Gilden
Date: 10-07-2023
"""


def is_kind_of_class(obj, a_class):
    """Determines if object {obj} is an instance of class {a_class} including
    subclasses

    Return:
        True: if {obj} is an instance of {a_class} or it's subclasses
        False: otherwise
    """
    return isinstance(obj, a_class)
