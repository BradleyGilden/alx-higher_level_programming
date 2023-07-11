#!/usr/bin/python3

"""
This module contains the function class_to_json()

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""


def class_to_json(obj):
    """returns dictionary representation of object of JSON serialization

    Args:
        obj(serializable): object from which __dict__ is returned
    """
    return obj.__dict__
