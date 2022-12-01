#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    n = len(sys.argv)

    if n != 3:
        print("Usage: ./100-my_calculator.py <a> operator <b>")
        sys.exit(1)

    operators = ["+", "-", "*", "/"]
    if operator != operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    add(a, b)
    sub(a, b)
    mul(a, b)
    div(a, b)
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

