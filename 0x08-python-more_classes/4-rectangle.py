#!/usr/bin/python3
""" a Rectangle class created by @Jr Hirwa on Apr 5"""


class Rectangle:
    """Represents a rectangle with a width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle.

        Raises:
            TypeError: If the value passed is not an integer.
            ValueError: If the value passed is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be greater than or equal to 0.")
        self._width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle.

        Raises:
            TypeError: If the value passed is not an integer.
            ValueError: If the value passed is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be greater than or equal to 0.")
        self._height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return (self._width * self._height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return ((self._width * 2) + (self._height * 2))

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: The printable representation of the rectangle with the
            # character.
        """
        if self._width == 0 or self._height == 0:
            return ""

        rect = []
        for i in range(self._height):
            [rect.append('#') for j in range(self._width)]
            if i != self._height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns a string representation of the rectangle object.

        Returns:
            str: The string representation of the rectangle object.
        """
        rect = "Rectangle(" + str(self._width)
        rect += ", " + str(self._height) + ")"
        return rect
