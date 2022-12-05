#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    def is_multiple_2(x):
        return x % 2 == 0

    result = map(is_multiple_2, my_list)

    return list(result)
