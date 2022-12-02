#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = my_list.index(idx+1)
    my_list = my_list[:i]+[element]+my_list[i+1:]
    print(my_list)
