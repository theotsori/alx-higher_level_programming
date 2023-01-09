#!/usr/bin/python3
"""a function that returns true if obj is instance"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of the specified class or
    a subclass of the specified class, and False otherwise
    """
    return isinstance(obj, a_class)
