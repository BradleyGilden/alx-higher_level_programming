#!/usr/bin/python3
"""
Module Contains a Locked class

Author: Bradley Dillion Gilden
Date: 04/07/2023
"""


class LockedClass:
    """
    Prevents users from dynamically creating new instance attributes
    """

    __slots__ = ["first_name"]
