#!/usr/bin/python3
import sys


sys.path.append("/home/nightlock/workspace/Python/alx-higher_level_programming/0x0A-python-inheritance")
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
