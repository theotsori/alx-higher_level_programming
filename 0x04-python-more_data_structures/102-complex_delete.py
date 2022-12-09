#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return {key: a_dictionary[key] for key in a_dictionary if a_dictionary[key] != value}
