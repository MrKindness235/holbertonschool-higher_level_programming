#!/usr/bin/python3
for c in range(97, 122):
    if c == 101 or c == 113:
        print("", end="")
    print("{}".format(chr(c)), end="")
