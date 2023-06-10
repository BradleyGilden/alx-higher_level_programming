#!/usr/bin/python3

# find maximum integer in list

def max_integer(my_list=[]):
    if my_list == []:
        return None

    max = my_list[0]

    for num in my_list:
        max = num if num > max else max

    return max


my_list = []
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
