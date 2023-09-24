#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    len = len(sys.argv)
    if len == 1:
        print("0 arguments.")
    elif len == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len - 1))
        for argument in sys.argv[1:]:
            print("{}: {}".format(i, argument))
            i += 1
