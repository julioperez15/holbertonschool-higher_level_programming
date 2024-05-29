#!/usr/bin/python3
""" my module class """


class Student():
    """ all my class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ public method """
        empty_dic = {}

        dicty = self.__dict__

        if attrs is None:
            return dicty

        if attrs:
            for elem in range(len(attrs)):
                if attrs[elem] in dicty:
                    empty_dic[attrs[elem]] = dicty[attrs[elem]]
            return empty_dic
        else:
            return empty_dic
