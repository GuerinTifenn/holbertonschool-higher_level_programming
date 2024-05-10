#!/usr/bin/python3

argc = len(argv) - 1

if __name__ == "__main__":
    import argv
    if argc <= 1:
        print("{} argument.".format(argc))
    else:
        print("{} arguments:".format(argc))
    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))
