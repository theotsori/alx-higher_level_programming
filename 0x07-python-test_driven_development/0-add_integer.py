#!/usr/bin/python3
"""
   A module that adds two integers
   takes a and b as integers or floats
   and adds them together
"""

def add_integer(a, b=98):
    """Python script that adds two integers

    Parameters:
    a (int or float): The first number to be added.
    b (int or float): The second number to be added. default is 98.

    Returns:
    int: The sum of a and b, casted into int

    Raises:
    TypeError: if a or b are not int or floats"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
