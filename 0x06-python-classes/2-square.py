#!?usr/bin/python3
# -*- coding: utf-8 -*-

class Square:
    """Square Class

    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0):
        """__init__ method of Square Class

        Args:
            size: (:obj: 'int', optional): private size instance

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size mus be >= 0")
        else:
            self.__size = size
