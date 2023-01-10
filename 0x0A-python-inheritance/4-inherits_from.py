#!/usr/bin/python3
"""Object function that returns if obj isinstance"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of the specified class or
    a subclass of the specified class
    """
    if isinstance(obj, a_class):
        return True
