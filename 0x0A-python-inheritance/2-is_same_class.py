#!/usr/bin/python3
"""A function that returns True if object is instance"""


def is_same_class(obj, a_class):
    """
    Return True if the object is an instance of the specified class,
    and False otherwise
    """
    return isinstance(obj, a_class)
