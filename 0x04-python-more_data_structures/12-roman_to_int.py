#!/usr/bin/python3
def roman_value(main_string):
    """ To assign the numbers to the right roman numeral """
    roman = [('I', 1), ('V', 5), ('X', 10),('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
    for items in roman:
        key, element = items
        if main_string is key:
            return element
    return None
def next_roman(numeral, index):
    """ checks the next character in the string and assigns the right number to the given roman numeral """
    if index + 1 < len(numeral):
        return roman_value(numeral[index + 1])
    else:
        return None
def roman_to_int(roman_string):
    result = 0
    if (roman_string is None or isinstance(roman_string, str) is False):
        return result
    order = enumerate(roman_string)
    for key, element in order:
        first = roman_value(element)
        second = next_roman(roman_string, key)
        if second is None or first >= second:
            result = result + first
        else:
            result = result + (second - first)
            next(order)
    return result
