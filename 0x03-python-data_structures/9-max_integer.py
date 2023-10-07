#!/usr/bin/python3
# find max num

def max_integer(my_list=[]):
    '''function that finds the biggest integer of a list'''
    if not my_list:  # Check if the list is empty
        return None
    else:
        max_num = my_list[0]  # Initialize max_num with the first element

        for num in my_list:
            if num > max_num:
                max_num = num  # Update max_num when a larger number is found

        return max_num
