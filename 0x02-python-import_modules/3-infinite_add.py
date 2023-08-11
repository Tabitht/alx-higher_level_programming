#!/usr/bin/python3
if __name__ == "__main__":
     import sys
     argv = sys.argv[1:]
     Len = len(argv)
     second = 0
     for i in range(Len):
          first = int(argv[i])
          second = first + second
     print("{:d}".format(second))
     