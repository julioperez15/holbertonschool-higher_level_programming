#!/usr/bin/python3


class MyList(list):
    """A class that inherits from the list class"""
    def print_sorted(self):
        """Prints the list, but sorted"""
        print(sorted(self))