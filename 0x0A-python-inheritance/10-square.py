#!/usr/bin/python3

'''
This script defines a BaseGeometry class with methods for area calculation and integer value validation, a Rectangle class that inherits from BaseGeometry, and a Square class that inherits from Rectangle.
'''

class BaseGeometry:
    '''
    Class: BaseGeometry
    Purpose:
        - Serves as a base class for geometrical operations.
        - Contains methods for area calculation and integer value validation.
    Methods:
        - area(self): Placeholder method raising an Exception if not implemented in the child class.
        - integer_validator(self, name, value): Validates if a value is an integer and greater than zero.
    '''
    def area(self):
        '''
        Method: area
        Arguments:
            - self: The instance of BaseGeometry
        Raises:
            - Exception: Indicates that 'area()' method is not implemented
        '''
        raise Exception("area() is not implemented")  # Placeholder method that raises an exception

    def integer_validator(self, name, value):
        '''
        Method: integer_validator
        Arguments:
            - self: The instance of BaseGeometry
            - name: Name of the variable to validate
            - value: Value to be validated
        Raises:
            - TypeError: Indicates that the value must be an integer
            - ValueError: Indicates that the value must be greater than 0
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))  # Raises an error if the value is not an integer
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))  # Raises an error if the value is not greater than 0

class Rectangle(BaseGeometry):
    '''
    Class: Rectangle
    Inherits from: BaseGeometry
    Purpose:
        - Represents a rectangle and inherits BaseGeometry's integer value validation methods.
    Attributes:
        - __width: Width of the rectangle
        - __height: Height of the rectangle
    '''
    def __init__(self, width, height):
        '''
        Method: __init__
        Arguments:
            - self: The instance of Rectangle
            - width: Width of the rectangle
            - height: Height of the rectangle
        Purpose:
            - Initializes the Rectangle object with width and height attributes after validating them.
        '''
        self.integer_validator("width", width)  # Validates the width
        self.integer_validator("height", height)  # Validates the height
        self.__width = width  # Sets the width attribute
        self.__height = height  # Sets the height attribute

    def __str__(self):
        '''
        Method: __str__
        Arguments:
            - self: The instance of Rectangle
        Returns:
            - A formatted string indicating the width and height of the rectangle
        '''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)  # Formats and returns string representation

    def area(self):
        '''
        Method: area
        Arguments:
            - self: The instance of Rectangle
        Returns:
            - The area of the rectangle (width * height)
        '''
        return self.__height * self.__width  # Calculates and returns the area of the rectangle

class Square(Rectangle):
    '''
    Class: Square
    Inherits from: Rectangle
    Purpose:
        - Represents a square and inherits from Rectangle, ensuring both sides are equal.
    Attribute:
        - __size: Size of the square (equal sides)
    '''
    def __init__(self, size):
        '''
        Method: __init__
        Arguments:
            - self: The instance of Square
            - size: Size of the square
        Purpose:
            - Initializes the Square object with size attribute after validating it and sets equal sides (width and height) using super() to call the parent's initialization.
        '''
        self.integer_validator("size", size)  # Validates the size
        self.__size = size  # Sets the size attribute
        super().__init__(self.__size, self.__size)  # Calls the parent's __init__ to set width and height as equal sides
