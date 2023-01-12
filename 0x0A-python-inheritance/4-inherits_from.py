#!/usr/bin/python3
"""Object function that returns if obj isinstance"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of the specified class or
    a subclass of the specified class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
