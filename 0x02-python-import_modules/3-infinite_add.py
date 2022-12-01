#!/usr/bin/python3
def sum_all(*args):
    sum = 0

    for s in args:
        num = str(s)
        if not num.isdigit():
            return False
        else:
            sum += int(num)
    return sum

if __name__ == "__main__":
    sum(int(*args))
