#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 4 00:48:12 2023
@author: Jr Hirwa
"""


class Rectangle:
    """Class Rectanle for defining a rectangular shape

    Attributes:
        empty
    """

    def __init__(self, width=0, height=0):
        """__init method for Rectangle class

        Attributes:
            width: (int, optional): for rectangle width
            height: (int, optional): for rectangle height
        """

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """get height property

        Returns:
            height (int): rectangle height
        """
        return self.__height

    @height.setter
    def height(self, result):
        """rectangle height Setter

        Attributes:
            height (int): rectangle height

        Raises:
            TypeError: when height is not an integer
            ValueError: when height is less than 0
        """
        if type(result) is not int:
            raise TypeError("height must be integer")
        elif result < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = result

    @property
    def width(self):
        """get width property

        Returns:
            width (int): rectangle width
        """
        return self.__width

    @width.setter
    def width(self, result):
        """rectangle width setter

        Attributes:
            width (int): rectangle width

        Raises:
            TypeError: when width is an integer
            ValueError: when width is less than 0
        """
        if type(result) is not int:
            raise TypeError("width must be an integer")
        elif result < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = result
