#!/usr/bin/python3
"""function that adds a new attribute to an object"""


def add_attribute(obj, name, value):
    """Implementation of the function"""
    if not hasattr(obj, '__setattr__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
