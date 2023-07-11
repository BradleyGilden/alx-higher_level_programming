#!/usr/bin/python3
import sys


sys.path.append("/home/nightlock/workspace/Python/alx-higher_level_programming/0x0B-python-input_output")
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "json_files/my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "json_files/my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "json_files/my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "json_files/my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
