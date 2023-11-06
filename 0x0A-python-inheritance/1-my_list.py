#!/usr/bin/python3

'''
This script defines a custom class 'MyList' that inherits from the 'list' class and includes a method to print the sorted elements of the list.
'''

class MyList(list):
    '''
    Class: MyList
    Inherits from: list
    Methods:
        - print_sorted: Prints the sorted elements of the list
    '''

    def print_sorted(self):
        '''
        Method: print_sorted
        Arguments:
            - self: The instance of MyList
        Purpose:
            Prints the sorted elements of the list
        '''
        print(sorted(self))  # Prints the elements of the list in sorted order
