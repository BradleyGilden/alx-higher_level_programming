#!/usr/bin/python3

# return a sorted dictionary based on key strings
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")
