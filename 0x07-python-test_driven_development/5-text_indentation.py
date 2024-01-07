#!/usr/bin/python3
def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :
    args:
        text - string to be printed
    Error to raise:
        TypeError - if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    count = 0
    while count < len(text) and text[count] == ' ':
        count += 1
    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
            while count < len(text) and text[count] == ' ':
                count += 1
            continue
        count += 1
