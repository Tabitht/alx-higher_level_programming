#!/usr/bin/python3
for k in range(97, 123):
    if k == 101 or k == 113:
        continue
    else:
        print("{:c}".format(k), end="")
