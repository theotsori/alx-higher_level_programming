#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):

        new_list = my_list[:idx]

        new_list += my_list[idx+1:]
        return new_list
    else:
        return my_list
