#!/usr/bin/bash
def remove_char_at(str, n):
    new_str = ""
    for count, c in enumerate(str):
        if (count != n):
            new_str += c
    return (new_str)
