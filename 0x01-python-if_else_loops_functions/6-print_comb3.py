#!/usr/bin/python3

# display numbers from 00 to 99
# numbers should  not be repeated like 00, 11, 22
# sequences should not be repeated like 10 and 01
for i in range(0, 10):
    for j in range(0, 10):
        if (j > i):
            if (i == 8 and j == 9):
                print("{0:d}{1:d}".format(i, j))
                exit(0)
            else:
                print("{0:d}{1:d}".format(i, j), end=", ")
