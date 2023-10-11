#!/usr/bin/python3
# 5-no_c


def no_c(my_string):
    """Remove characters c and C from a string"""
    noC_string = [char for char in my_string if char != 'c' and char != 'C']
    return ("".join(noC_string))
