#!/usr/bin/python3
""" Function that insets a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Implementation of search and update"""
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string + '\n')
    with open(filename, 'w') as file:
        file.writelines(lines)
