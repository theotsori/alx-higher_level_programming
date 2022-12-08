#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    integer = 0
    previous_value = 0
    for ch in roman_string[::-1]:
        current_value = roman_to_int_map[ch]
        if current_value < previous_value:
            integer -= current_value
        else:
            integer += current_value
        previous_value = current_value

    return integer
