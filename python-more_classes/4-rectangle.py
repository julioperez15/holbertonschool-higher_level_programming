#!/usr/bin/python3
"""Module that defines a class"""


class Rectangle:
    """a class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """returns the string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for i in range(self.height)])

    def __repr__(self):
        """returns the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """prints a message when an instance is deleted"""
        print("Bye rectangle...")
