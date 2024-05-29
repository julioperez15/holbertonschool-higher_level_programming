#!/usr/bin/python3
""" module write a file """


def write_file(filename="", text=""):
    """text to write"""
    with open(filename, 'w', encoding="utf-8") as files:
        return files.write(text)
