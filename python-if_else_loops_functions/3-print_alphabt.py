#!/usr/bin/python3
for c in range(97, 123):
    if c == 101 or c == 113:
        print("", end="")
    else:
        print("{}".format(chr(c)), end="")
