#!/usr/bin/python3

'''
This script defines a function 'is_same_class' that checks if the provided object is an instance of a given class.
'''

def is_same_class(obj, a_class):
    '''
    Function: is_same_class
    Arguments:
        - obj: The object to be checked
        - a_class: The class to compare against
    Returns:
        - True if the object is an instance of the given class, otherwise False
    '''
    if type(obj) is a_class:  # Checking if the type of the object matches the provided class
        return True
    else:
        return False
