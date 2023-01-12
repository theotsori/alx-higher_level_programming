#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys

count = 0
file_size = 0
status_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    for line in sys.stdin:
        count += 1
        data = line.strip().split()
        file_size += int(data[-1])
        status = int(data[-2])
        if status in status_count:
            status_count[status] += 1

        if count % 10 == 0:
            print("Total file size: ", file_size)
            for status_code in sorted(status_count):
                if status_count[status_code] > 0:
                    print(f"{status_code}: {status_count[status_code]}")
            print("\n")
except KeyboardInterrupt:
    print("Total file size: ", file_size)
    for status_code in sorted(status_count):
        if status_count[status_code] > 0:
            print(f"{status_code}: {status_count[status_code]}")
