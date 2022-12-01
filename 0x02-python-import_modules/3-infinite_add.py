#!/usr/bin/python3
import sys
n = len(sys.argv)
Sum = 0
for i in range(1, n):
    Sum += int(sys.argv[i])
if __name__ == "__main__":
    print(Sum)
