#!/usr/bin/python3

# multiplies values my 2 and returns a new dict
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key in new_dict.keys():
        new_dict[key] = new_dict[key] * 2

    return new_dict
