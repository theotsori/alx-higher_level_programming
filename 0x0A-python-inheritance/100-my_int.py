#!/usr/bin/python3
"""A calss that inherits from int"""


class MyInt(int):
    """MyInt is a rebel of eq and ne"""
    def __eq__(self, other):
        return not int.__eq__(self, other)

    def __ne__(self, other):
        return not int.__ne__(self, other)
