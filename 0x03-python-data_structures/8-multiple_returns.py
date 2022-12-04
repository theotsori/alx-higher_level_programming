#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None

    length = len(sentence)
    first = sentence[:1]

    return length, first;

    length, first = multiple_returns()

    print(length)
    print(first)
