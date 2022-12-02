def no_c(my_string):
    rm = ["c", "C"]
    s = ""
    for i in my_string:
        if i not in rm:
            s += i
    return str(s)
