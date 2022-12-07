#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # create a variable to store the key with big val
    # set it to the first key
    best_key = list(a_dictionary.keys())[0]
    for key in a_dictionary.keys():
        if a_dictionary[key] > a_dictionary[best_key]:
            best_key = key
    return best_key
