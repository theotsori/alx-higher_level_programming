#!/usr/bin/python3
"""function that returns list of list rep pascal tri"""


def pascal_triangle(n):
    """Implementation of the pascal triangle function"""
    if n <= 0:
        return []
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle
