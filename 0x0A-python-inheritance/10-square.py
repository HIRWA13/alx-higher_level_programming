#!/usr/bin/python3

"""
Python Module created by @Jr Hirwa
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class square shape that inherits from Rectangle and BaseGeometry classes
    """
    def __init__(self, size):
        """"
        Init function for Square class
        Attributes:
            size (int): size of square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
