#!/usr/bin/python3

class Square:
    """Square Class

    Attributes:
        size
    """
    def __init__(self, size=0):
        """__init__method of Square

        Arguments:
            self(default)
            size whixh is assigned to zero
        """
        if type(size) is not int:
            raise TypeError("Incorect Type, must be int")
        elif size < 0:
            raise ValueError("Size can not be less than Zero")
        else:
            self.__size = size

    def area(self):
        """are method to create area

        Arguments:
            self(default)
        Returns:
            The area of a square
        """
        return self.__size ** 2
