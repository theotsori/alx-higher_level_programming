#!/usr/bin/python3
"""A class LockedClass with no class or object attribute"""


class LockedClass:
    """A class Locked with no class"""
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value
