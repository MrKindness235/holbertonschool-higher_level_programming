#!/usr/bin/python3
from sqlalchemy import false


def is_same_class(obj, a_class):
    if a_class == object:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
