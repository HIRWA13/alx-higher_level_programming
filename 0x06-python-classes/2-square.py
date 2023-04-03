#!?usr/bin/python3

class Square:
    """Square Class

    Attributes:

        size
    """
    def __init__(self, size=0):
        """__init__ method

        Attributes:
            self
            size
        """
        if type(size) is not int:
            raise TypeError("Incorect Size format")
        elif size < 0:
            raise ValueError("Size can't be less than Zero(0)")
        else:
            self.__size = size
