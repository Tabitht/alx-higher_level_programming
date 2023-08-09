#!/usr/bin/python3
def uppercase(str):
    s = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            s += chr(ord(i) - 32)
        else:
            s += i
    print("{:s}".format(s), end="")
    print()
