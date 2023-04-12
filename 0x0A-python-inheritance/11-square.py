#!/usr/bin/python3

"""
module created by @Jr Hirwa
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    class Square shape that inheirts from BaseGeometry from task 9
    """
    def __init__(self, size):
        """"
        Init function for Square class
        Attributes:
            size (int): The size of  square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str funtion to print with and height
        Returns:
            Return width and height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        function that calculates area of the Square
        """
        return self.__size ** 2
