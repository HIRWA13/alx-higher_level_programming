#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 3 23:57:43 2023
@author: Jr Hirwa
"""


class Square:
    """Square Class

    Attributes:
        size (int): square size
    """
    def __init__(self, size=0):
        """__init__method of Square class

        Args:
            size: (:obj: 'int', optional): private instance size

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """areq method to create area

        Returns:
            The area of a square
        """
        return self.__size ** 2
