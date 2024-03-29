#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 3 21:46:54 2023
@author: Jr Hirwa
"""


class Square:
    """a Square class

    Attributes:
        size (int): size of int type to specifie the square size
    """
    def __init__(self, size):
        """the __init__ method for Square class

        Args:
            size: (:obj: 'int'): private size instance
        """
        self.__size = size
