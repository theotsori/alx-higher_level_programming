#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    n = chr(i)
    if n not in "qe":
        print(n, end="")
