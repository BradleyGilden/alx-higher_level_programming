#!/usr/bin/python3
import sys


sys.path.append("/home/nightlock/workspace/Python/alx-higher_level_programming/0x0A-python-inheritance")
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
