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
    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
        c += 1
