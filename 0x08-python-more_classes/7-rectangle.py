#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """
    Represents a rectangle object.

    Attributes:
        width (int): The width of the rectangle object.
        height (int): The height of the rectangle object.
        symbol (any): The symbol used to represent the rectangle object.
        instances_num (int): The number of instances of Rectangle.
    """

    instances_num = 0
    symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).instances_num += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be greater than or equal to zero.")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be greater than or equal to zero.")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle object."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle object."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle object."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Returns a string representation of the rectangle object."""
        rect_repr = (f"Rectangle({self.__width}, {self.__height})"        
        return rect_repr

    def __del__(self):
        """Deletes the rectangle object and decrements instances_num."""
        type(self).instances_num -= 1
        print("Bye rectangle...")
