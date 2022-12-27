#!/usr/bin/python3
def text_indentation(text):
    # check if text is a string
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    # iterate through the characters in the text
    for i, char in enumerate(text):
        # print the character
        print(char, end='')
        if char in ['.', '?', ':']:
            print('\n' * 2)
