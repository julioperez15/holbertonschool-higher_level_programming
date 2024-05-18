#!/usr/bin/python3
"""
Square: A class that defines a square by its size
and can calculate its area.
"""


class Square:
    """
    Square class with size attribute and area method.
    """

    def __init__(self, size=0):
        """
        Initialize square with size. Size must be an integer
        and >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size ** 2
