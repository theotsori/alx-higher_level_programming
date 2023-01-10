#!/usr/bin/python3
"""Function that writes string to a text file"""


def write_file(filename="", text=""):
    """Module that return number of characters written"""
    with open(filename, "w", encoding="utf8") as file:
        num_chars = file.write(text)
    return num_chars
