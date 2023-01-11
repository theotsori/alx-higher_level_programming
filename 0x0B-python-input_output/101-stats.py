#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys
from collections import defaultdict

status_codes = defaultdict(int)
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        status_code = parts[-3]
        file_size = int(parts[-1])
        total_size += file_size
        status_codes[status_code] += 1

        if line_count % 10 == 0:
            print("Total file size: ", total_size)
            for key in sorted(status_codes.keys()):
                print("{}: {}".format(key, status_codes[key]))
except KeyboardInterrupt:
    print("Total file size: ", total_size)
    for key in sorted(status_codes.keys()):
        print("{}: {}".format(key, status_codes[key]))
