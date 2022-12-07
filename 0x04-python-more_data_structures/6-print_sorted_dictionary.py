#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # get the keys of the dictionary as a list
    keys = list(a_dictionary.keys())
    # sort the list of keys
    keys.sort()
    # print the dictionary by iterating over the sorted keys
    for key in keys:
        print(f"{key}: {a_dictionary[key]}")
