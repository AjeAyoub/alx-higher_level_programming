#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    result = 0

    for x in uniq_list:
        result = result + x

    return (result)
