#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    index = 0
    for value in my_list:
        if value == search:
            new_list[index] = replace
        index += 1
    return (new_list)
