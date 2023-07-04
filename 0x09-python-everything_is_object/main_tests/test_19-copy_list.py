#!/usr/bin/python3
import sys


sys.path.append("/home/nightlock/workspace/Python/alx-higher_level_programming/0x09-python-everything_is_object")
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)
