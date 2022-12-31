#!/usr/bin/python3

def print_square(size):
    """
    Print a square made of # characters with the given size.

    Parameters:
    sie (int): The size of the sqaure. Must be an integer greater than or equal to 0.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is a negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
