#!/usr/bin/python3
"""Rectangle class created by @Jr Hirwa on Tue April 4."""


class Rectangle:
    """rectangle class.
    Attributes:
        num_of_instances (int):  Rectangle instances.
        symbol (any): The symbol used for string representation.
    """

    num_of_instances = 0
    symbol = "#"

    def __init__(self, width=0, height=0):
        """make another Rectangle.
        Args:
            width: new rectangle width.
            height: new rectangle height.
        """
        type(self).num_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and set Rectangle width."""
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
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rectangle_1, rectangle_2):
        """Return: Rectangle with the higher area.
        Args:
            rectangle_1:  first Rectangle.
            rectangle_2:  second Rectangle.
        Raises:
            TypeError: If rectangle_1 or rectangle_2 is not a Rectangle.
        """
        if not isinstance(rectangle_1, Rect):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rectangle_2, Rect):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rectangle_1.area() >= rectangle_2.area():
            return (rectangle_1)
        return (rectangle_2)

    @classmethod
    def square(cls, size=0):
        """Return: new Rectangle with width and height equal to size.
        Args:
            size (int): the new Rectangle width.
        """
        return (cls(size, size))

    def __str__(self):
        """Return or print a rectangle in form of #."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle_list = []
        for i in range(self.__height):
            [rectangle_list.append(str(self.symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle_list.append("\n")
        return ("".join(rectangle_list))

    def __repr__(self):
        """Return the string representation Rectangle."""
        rectangle_list = "Rectangle(" + str(self.__width)
        rectangle_list += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message anytime a Rectangle is deleted."""
        type(self).num_of_instances -= 1
        print("Bye rectangle...")

