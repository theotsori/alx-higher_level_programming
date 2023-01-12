#!/usr/bin/python3
"""function that adds a new attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """Implementation of the function"""
    if not hasattr(obj, '__setattr__'):
        raise AttributeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
