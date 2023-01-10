#!/usr/bin/python3
"""Function that appends string at the end of text file"""


def append_write(filename="", text=""):
    """Returns number of characters added"""
    with open(filename, "a", encoding="utf8") as file:
        num_chars = file.write(text)
    return num_chars
