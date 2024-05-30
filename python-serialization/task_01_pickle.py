#!/usr/bin/env python3

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = "John"
        self.age = 25
        self.is_student = True

    def __str__(self):
        return f"CustomObject: {self.name}, {self.age}, {self.is_student}"

    def __repr__(self):
        return f"CustomObject: {self.name}, {self.age} {self.is_student}"

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\
            \nIs Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as ouput_file:
                pickle.dump(self, ouput_file)
        except Exception as e:
            print(f"An error occurred while serializing the object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as input_file:
                return pickle.load(input_file)
        except Exception as e:
            print(f"An error occurred while deserializing the object: {e}")
            return None
