#!/usr/bin/python3

"""
contains function add_attribute

Author: Bradley Dillion Gilden
Date: 10-07-2023
"""


def add_attribute(obj, attr, value):
    """Add a new attribute to object unless __dict__ is unavailable

    Args:
        obj (any): The object to dynamically add attribute to
        attr (str): The name of the attribute
        value (any): value to be assigned to attribute
    Raises:
        TypeError: If the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
