#!/usr/bin/python3|

"""
Python Module created by @jr Hirwa
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry class
    """
    def __init__(self, width, height):
        """
        init function for Rectangle class
        Attributes:
            width (int): the width of  rectangle
            height (int): the height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        str funtion for rectangle
        Returns:
            Return width and height
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """
        function that calculates the area of the rectangle
        Return:
           The area of rectangle
        """
        return self.__width * self.__height
