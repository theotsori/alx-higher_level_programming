#!/usr/bin/python3
def uniq_add(my_list=[]):
    # create a set to store unique int
    unique_numbers = set()
    # iterate over list
    for i in my_list:
        # check if the number is not already in set
        if i not in unique_numbers:
            # if its not add to the set
            unique_numbers.add(i)

    # initiallize the result variable
    rel = 0
    # iterate over the set of unique nums
    for i in unique_numbers:
        # add current num to the result
        rel += i
    # Return result
    return rel
