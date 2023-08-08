#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        print("{:d}".format(i), end=", ")
        if i == 100:
            print("{:s}".format(i))
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=", ")
        if i % 3 == 0:
            print("Fizz", end=", ")
        if i % 5 == 0:
            print("Buzz", end=", ")
