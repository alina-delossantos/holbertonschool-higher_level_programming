#!/usr/bin/python3
"""JSON handling"""
import json


def from_json_string(my_str):
    """representation of python obj by Json"""
    deserialized_json = json.loads(my_str)
    return deserialized_json
