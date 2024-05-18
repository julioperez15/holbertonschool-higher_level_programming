#!/usr/bin/python3
"""
    This module defines a class Square.

    This module demonstrates the creation of a cass in Python that initializes
    a private instance attribute: size.
    """


class Square:
    """
    This is a class that defines a square.

    Attributes:
         __size (int): size of the side of the square.
    """
    def __init__(self, size):
        """
        The constructor for Square class.

        Parameters:
            size (int): size of the side of the square.

        """
        self.__size = size