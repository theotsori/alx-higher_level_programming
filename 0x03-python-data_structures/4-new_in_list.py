#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    i = my_list.index(idx+1)
    my_list = my_list[:i]+[element]+my_list[i+1:]
    return my_list
