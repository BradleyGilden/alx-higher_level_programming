#!/usr/bin/python3

for i in range(97, 123):  # prints lower ASCII alphabet except e and q
    if i != 101 and i != 113:
        print("{0:c}".format(i), end="")
