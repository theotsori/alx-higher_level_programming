#!/usr/bin/python3
""" Function that insets a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Implementation of search and update"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + "\n")
