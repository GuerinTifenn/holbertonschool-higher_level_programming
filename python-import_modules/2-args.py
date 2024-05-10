#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1

if __name__ == "__main__":
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
