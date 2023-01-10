#!/usr/bin/python3
"""A module that reads a text file"""


def read_file(filename=""):
    """Function that reads a file"""
    with open(filename, "r", encoding="utf8") as f:
        print(f.read())
