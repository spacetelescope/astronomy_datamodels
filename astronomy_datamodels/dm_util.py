# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import numpy as np

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
    if not isinstance(tuple, stype):
        st = [stype]
    
    for item in arg:
        fail = True
        for stype in st:
            if isinstance(item, stype):
                fail = False
        if fail:
            raise ValueError("Sequence must contain only {}".format(str(stype)))

def convert_to_array(value, dtype=None):
    if dtype is None:
        dtype = np.float
    try:
        value = np.array(value, dtype)
    except ValueError:
        raise ValueError("supplied value must be convertable to numpy array")

    return value