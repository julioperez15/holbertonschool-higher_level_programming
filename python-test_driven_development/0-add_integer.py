#!/usr/bin/python3
"""
Task: 0-add_integer
Test: Cases for unittest
Args: a+b
"""


def add_integer(a, b=98):
    """Adds two numbers after converting them to integers,
    raises TypeError if inputs are not numbers.
    >>> add_integer(2,3)
    5
    >>> add_integer(5,5)
    10
    >>>
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(0, {})
    Traceback (most recent call last):
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
