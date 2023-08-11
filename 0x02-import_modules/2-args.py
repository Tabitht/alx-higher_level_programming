#!/usr/bin/python3
if __name__ == "__main__":
     import sys
     argv = sys.argv[1:]
     Len = len(argv)
     i = 1
     if Len == 0:
          print("{:d} arguments.".format(Len))
     elif Len == 1:
           print("{:d} argument:".format(Len))
           print("{:d}: {:s}".format(i, argv[0]))
     else:
          print("{:d} arguments:".format(Len))
          while i <= Len:
               print("{:d}: {:s}".format(i, argv[i - 1])) 
               i = i + 1