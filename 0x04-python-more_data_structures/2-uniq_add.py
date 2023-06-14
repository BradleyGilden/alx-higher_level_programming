#!/usr/bin/python3

# add unique elements in list
def uniq_add(my_list=[]):
    sum = 0

    if my_list == []:
        return my_list

    for num in set(my_list):
        sum += num

    return sum
