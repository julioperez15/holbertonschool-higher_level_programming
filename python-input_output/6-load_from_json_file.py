#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """method to create for the  object"""
    with open(filename, 'r', encoding="utf-8") as write:
        return json.load(write)
