#!/usr/bin/python3
for i in range(97, 123):
    n = chr(i)
    if n not in "eq":
        print("{}".format(n), end="")
