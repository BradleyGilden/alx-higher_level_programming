#!/usr/bin/python3
import sys


sys.path.append("/home/nightlock/workspace/Python/alx-higher_level_programming/0x0A-python-inheritance")
lookup = __import__('0-lookup').lookup


class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
