#!/usr/bin/python3
for i in range(0, 10):
    for k in range(0, 10):
        if i < k:
            if i == 8 and k == 9:
                break
            print("{}{}".format(i, k), end=", ")
n = 89
print(n, end="\n")
