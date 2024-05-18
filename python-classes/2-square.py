#!/usr/bin/python3
"""
This module defines a class Square.
The Square class defines a square by its size, which defaults
to 0 if not provided.
"""


class Square:
    """
    A class that defines a square by its size.

    ...
    Attributes
    ----------
    size : int
        size of the square, default to 0
    Methods
    -------
    __init__(self, size=0):
        Initalizes the square
    """
    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
            size : int
                size of the square, defaults to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
