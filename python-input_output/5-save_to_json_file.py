#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """json reprentation whithin a file """
    with open(filename, "w", encoding="utf-8") as write_file:
        json.dump(my_obj, write_file)
