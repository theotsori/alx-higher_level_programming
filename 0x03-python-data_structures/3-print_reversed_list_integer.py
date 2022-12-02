#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    r_list = []
    for i in my_list:
        r_list.insert(0, i)
    for x in range(len(r_list)):
        print(r_list[x], sep="\n")
