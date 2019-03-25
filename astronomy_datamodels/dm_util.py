# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

def check_int_sequence(arg, length=None):
    if arg is None:
        return
    if length is not None:
        if len(arg) != length:
            raise ValueError("Must be a sequence of length {}".format(length))
    for item in arg:
        if not isinstance(item, int):
            raise ValueError("Sequence must contain only integers")

def check_sequence_type(arg, stype, length=None):
    if arg is None:
        return
    if length is not None:
        if len(arg) != length:
            raise ValueError("Must be a sequence of length {}".format(length))
    for item in arg:
        if not isinstance(item, stype):
            raise ValueError("Sequence must contain only {}".format(str(stype)))
