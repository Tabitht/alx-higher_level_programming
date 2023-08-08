#!/usr/bin/python3
for i in range(10):
    for k in range(10):
        if i >= k:
            continue
        if i == 8 and k == 9:
            print("{:d}{:d}".format(i, k))
        else:
            print("{:d}{:d}".format(i, k), end=", ")
