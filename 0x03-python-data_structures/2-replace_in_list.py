#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    while i < len(my_list):
        if my_list[i] == idx:
            my_list[i] = element
        i += 1
    print(my_list)
