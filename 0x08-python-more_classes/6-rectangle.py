#!/usr/bin/python3

"""This module defines a Rectangle class that
    represents a 2D rectangular shape."""


class Rectangle:
    """
    A Rectangle class to represent a 2D rectangular shape.

    Attributes:
        instances_num (int): The number of Rectangle instances.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a new Rectangle instance.
        area(self): Calculates and returns
            the area of the Rectangle instance.
        perimeter(self): Calculates and returns
            the perimeter of the Rectangle instance.
        __str__(self): Returns a string representation
            of the Rectangle instance.
        __repr__(self): Returns a string representation
            of the Rectangle instance that can be used to recreate it.
        __del__(self): Destroys the Rectangle instance and
            updates the count of instances_num.

    """

    instances_num = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance
            with specified width and height.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).instances_num += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        The width of the Rectangle instance.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        The height of the Rectangle instance.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the Rectangle instance.

        Returns:
            int: The area of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates and returns the perimeter of the Rectangle instance.

        Returns:
            int: The perimeter of the Rectangle instance.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        The string representation represents the rectangle with the
            # character.

        Returns:
            str: A string representation of the Rectangle instance.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """
        Returns a string representation of the Rectangle instance that
        can be used to recreate it.

        Returns:
            str: A string representation of the Rectangle instance that
            can be used to recreate it.
        """
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Print a message for everytime a Rectangle is deleted."""
        type(self).instances_num -= 1
        print("Bye rectangle...")
