#!/usr/bin/python3

# adds 2 tuples

def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)

    a1 = tuple_a[0] if a_len >= 1 else 0
    a2 = tuple_a[1] if a_len >= 2 else 0
    b1 = tuple_b[0] if b_len >= 1 else 0
    b2 = tuple_b[1] if b_len >= 2 else 0

    new_tuple = (a1 + b1, a2 + b2)

    return new_tuple
