#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1

if __name__ == "__main__":
    if argc <= 1:
        print("{} argument.".format(argc))
    else:
        print("{} arguments:".format(argc))
    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))
