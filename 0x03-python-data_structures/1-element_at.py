#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    while i < len(my_list):
        if idx < 0:
            return None
        elif idx > len(my_list) or idx == len(my_list):
            return None
        else:
            return my_list[idx]
        i = i + 1
