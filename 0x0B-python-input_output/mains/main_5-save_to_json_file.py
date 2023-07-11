#!/usr/bin/python3
import sys


sys.path.append("/home/nightlock/workspace/Python/alx-higher_level_programming/0x0B-python-input_output")
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "json_files/my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "json_files/my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "json_files/my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
