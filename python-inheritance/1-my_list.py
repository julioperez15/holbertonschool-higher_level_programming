#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Generates a new class that inherits attributes and
    methods of the baseclass list"""

    def print_sorted(self):
        """Prints the sorted list: ascending order"""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
