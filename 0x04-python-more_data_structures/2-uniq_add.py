#!/usr/bin/python3
def uniq_add(my_list=[]):
    j = 0
    for i in my_list:
        k = i
        k = i + j
        j = k
    return j
