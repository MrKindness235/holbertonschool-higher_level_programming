#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    if len(sys.argv) == 1:
        print("0")
    else:
        for argument in sys.argv[1:]:
            result += int(argument)
        print("{}".format(result))
