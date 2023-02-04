#!/usr/bin/python3
"""
   A function that divides all elemnts of a matrix
   Checks whether it is an integer or not.
"""
def matrix_divided(matrix, div):
    """
       Check if div is a number
       Check if div is not equal to 0
       Check if the matrix is list of lists of integers or floats
       Check if each row of the matrix has the same size
       Divide all elements of the matrix by div and round to 2 dec places
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integer/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
