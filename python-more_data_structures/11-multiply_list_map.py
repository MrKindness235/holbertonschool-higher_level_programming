#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    for index in new_list:
        new_list[index] = new_list[index] * number
