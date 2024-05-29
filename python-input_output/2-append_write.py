#!/usr/bin/python3
""" module to append text """


def append_write(filename="", text=""):
    """ appends a string to the end of file """
    with open(filename, mode="a", encoding='utf-8') as file:
        return file.write(text)
