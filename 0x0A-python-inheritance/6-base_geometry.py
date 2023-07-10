#!/usr/bin/python3

"""
This is the Geometry module containing class: BaseGeometry

Author: Bradley Dillion Gilden
Date: 10-07-2023
"""


class BaseGeometry:
    """This class contains a single instance function area()

    Raises:
        Exception: when area() is called"""

    def area(self):
        """raises an Exception always"""
        raise Exception("area() is not implemented")
