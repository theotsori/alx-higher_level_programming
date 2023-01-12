#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys

total_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split(" ")
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        total_size += file_size
        if status_code in status_code_count:
            status_code_count[status_code] += 1
        if line_count % 10 == 0:
            print("Total file size: ", total_size)
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print(f"{code}: {status_code_count[code]}")
except KeyboardInterrupt:
    print("Total file size: ", total_size)
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")
