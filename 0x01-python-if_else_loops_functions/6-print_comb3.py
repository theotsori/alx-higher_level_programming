#!/usr/bin/python3
for i in range(0, 10):
    for k in range(0, 10):
        if i < k:
            print("{}{}".format(i, k), end=", ")
