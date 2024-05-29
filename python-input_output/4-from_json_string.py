#!/usr/bin/python3
""" module json """
import json


def from_json_string(my_str):
    """convert json to pytohn dict"""
    return json.loads(my_str)
