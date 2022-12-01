#!/usr/bin/python3
import sys
n = len(sys.argv)
for i in range(1, n):
    if n == 1 in range(1, n):
        print("0 arguments.")
    if n == 2:
        print("{} argument:\n{}: {}".format(n, n, sys.argv[i]))
    else:
        print("{}: {}".format(n, sys.argv[i]))
