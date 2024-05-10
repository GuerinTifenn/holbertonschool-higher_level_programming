#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    args = argv[1:]  # Exclude script name from arguments
    result = sum(map(int, args))
    print("{}".format(result))
