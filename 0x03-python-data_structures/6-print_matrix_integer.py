#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cal in row:
            print("{:d}".format(cal), end=" ")
        print()
