#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv[1:]
    Len = len(argv)
    if Len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[0])
        b = int(argv[2])
        i = argv[1]
        if i == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif i == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif i == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif i == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
