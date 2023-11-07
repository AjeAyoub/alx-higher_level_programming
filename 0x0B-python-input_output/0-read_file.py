#!/usr/bin/python3

"""Defines a function for reading and displaying the contents of a text file."""

def read_file(filename=""):
    """
    Reads the content of a UTF-8 encoded text file and prints it to the standard output.
    
    Args:
        filename (str): The name of the file to be read. Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
