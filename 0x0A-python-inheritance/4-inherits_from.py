#!/usr/bin/python3

'''
This script defines a function 'inherits_from' that checks if the provided object inherits from a given class (or its subclasses).
'''

def inherits_from(obj, a_class):
    '''
    Function: inherits_from
    Arguments:
        - obj: The object to be checked
        - a_class: The class to compare against for inheritance
    Returns:
        - True if the object inherits from the given class (or its subclasses), otherwise False
    '''
    if type(obj) is not a_class and isinstance(obj, a_class):  # Checking if the object is not of the exact class and is an instance of the given class or its subclass
        return True
    else:
        return False
