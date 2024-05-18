#!/usr/bin/python3
"""
Module for Square class.
"""


class Square:
    """
    Square class with size attribute and area calculation.
    """

    def __init__(self, size=0):
        """Initialize Square with optional size."""
        self.__size = size

    def area(self):
        """Calculate and return the area of the Square."""
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square, with checks for valid size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value
