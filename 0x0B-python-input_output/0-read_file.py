#!/usr/bin/python3
"""A module that reads a text file"""


def read_file(filename=""):
    """Function that reads a file"""
    with open('my_file_0.txt', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
