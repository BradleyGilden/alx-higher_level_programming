#!/usr/bin/python3
# removes char at index
def remove_char_at(str, n):
    if str is None:
        return None
    if n > len(str) or n < 0:
        return str

    str = str[:n] + str[n + 1:]
    return str
