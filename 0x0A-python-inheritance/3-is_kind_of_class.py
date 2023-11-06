#!/usr/bin/python3

'''
This script defines a function 'is_kind_of_class' that checks if the provided object is an instance of the given class or a subclass.
'''

def is_kind_of_class(obj, a_class):
    '''
    Function: is_kind_of_class
    Arguments:
        - obj: The object to be checked
        - a_class: The class to compare against
    Returns:
        - True if the object is an instance of the given class or a subclass, otherwise False
    '''
    if isinstance(obj, a_class):  # Checking if the object is an instance of the given class or a subclass
        return True
    else:
        return False
