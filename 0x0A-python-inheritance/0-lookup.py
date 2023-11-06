#!/usr/bin/python3

'''
This script defines a function 'lookup' that retrieves a list of attributes and methods associated with a given object.
'''

def lookup(obj):
    '''
    Function: lookup
    Arguments:
        - obj: The object for which attributes and methods are to be retrieved
    Returns:
        - A list of attributes and methods associated with the provided object
    '''
    return dir(obj)  # Returns a list of attributes and methods associated with the provided object
