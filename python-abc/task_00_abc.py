#!/usr/bin/env python3


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    A class representing a dog.

    Attributes:
        _sound (str): The sound that a dog makes.
    """

    def __init__(self):
        self._sound = "Bark"

    def sound(self):
        """
        Returns the sound that a dog makes.

        Returns:
            str: The sound of a dog.
        """
        return self._sound


class Cat(Animal):
    def __init__(self):
        self._sound = "Meow"

    def sound(self):
        return self._sound
