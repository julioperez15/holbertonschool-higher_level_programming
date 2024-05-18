#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size.
Size can be accessed or modified through the public methods of the class.
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """Initializes the square with a given size."""
        self.__size = size

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
