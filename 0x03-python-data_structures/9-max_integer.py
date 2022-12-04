def max_integer(my_list=[]):
    if my_list == "":
        return None

    mi = my_list[0]

    for x in my_list:
        if x > mi:
            mi = x
    return mi
