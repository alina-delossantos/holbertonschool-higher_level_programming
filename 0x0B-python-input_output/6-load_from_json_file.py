#!/usr/bin/python3
"""creates an Object"""
import json


def load_from_json_file(filename):
    """
    creates an Object from JSONfile
    """
    with open(filename, encoding="utf-8") as f:
        new_obj = json.load(f)
    return new_obj
