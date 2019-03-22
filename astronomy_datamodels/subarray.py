# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from .dm_util import check_sequence_type

class Subarray:

    def __init__(self, offset, size, name=None):
        self.offset = offset
        self.size = size
        self.name = name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        check_sequence_type(value, stype=int, length=2)
        self._size = value

    @property
    def offset(self):
        return self._offset
    
    @offset.setter
    def offset(self, value):
        check_sequence_type(value, stype=int, length=2)
        self._offset = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value