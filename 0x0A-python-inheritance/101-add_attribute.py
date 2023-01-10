#!/usr/bin/python3

def add_attribute(obj, attr_name, attr_value):
    if not hasattr(obj, '__setattr__'):
        raise AttributeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
