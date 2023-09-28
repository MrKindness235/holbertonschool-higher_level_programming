#!/usr/bin/python3
def uniq_add(my_list=[]):
    result, unique = 0, set(my_list)
    for value in unique:
        result += value
    return (result)