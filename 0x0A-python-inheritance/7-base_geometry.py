#!/usr/bin/python3

"""
Python Module created by @Jr Hirwa
"""


class BaseGeometry():
    """
    An empty BaseGeomentry class
    """
    pass

    def area(self):
        """
        a function calculates the area
        Raises:
            Exception if area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
         function that validates integer input
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
