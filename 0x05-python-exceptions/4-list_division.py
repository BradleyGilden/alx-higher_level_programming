#!/usr/bin/python3

"""
safe_print_list - divides 2 lists element by element
@my_list_1: divident list
@my_list_2: divisor list
@list_length: length of list
Return: list of divided elements
"""


def list_division(my_list_1, my_list_2, list_length) -> list:
    result = []
    res = 0
    i = 0
    while i < list_length:
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(res)
            i += 1
    return result
