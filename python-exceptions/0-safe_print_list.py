#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        for index in range(0, x + 1):
        try:
            print("{}".format(my_list[index]))
        except IndexError:
            break