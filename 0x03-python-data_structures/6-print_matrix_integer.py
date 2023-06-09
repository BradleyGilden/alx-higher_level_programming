#!/usr/bin/python3

# print an integer matrix
def print_matrix_integer(matrix=[[]]):

    if matrix == [[]]:
        print()
        return

    for row in matrix:
        for i in range(len(row)):
            if i != len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]))
