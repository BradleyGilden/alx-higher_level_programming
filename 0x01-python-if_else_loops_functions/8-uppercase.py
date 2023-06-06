#!/usr/bin/python3
def uppercase(str):  # converts string to uppercase
    endchar = ""
    i = 1
    if str != "":
        for c in str:
            if i == len(str):
                endchar = "\n"
            if ord(c) >= 97 and ord(c) <= 122:
                c = chr(ord(c) - 32)
            print("{}".format(c), end=endchar)
            i += 1
