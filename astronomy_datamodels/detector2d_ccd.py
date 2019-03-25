# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from .dm_util import check_sequence_type
from .subarray import Subarray

class Detector2dCCD:

    def __init__(self, name, size, binning=None, subarray=None,
                 meta=None):
        self.name = name
        self.size = size
        self.binning = binning
        self.subarray = subarray
        self.meta = meta

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        check_sequence_type(value, stype=int, length=2)
        self._size = value

    @property
    def binning(self):
        return self._binning

    @binning.setter
    def binning(self, value):
        check_sequence_type(value, stype=int, length=2)
        self._binning = value

    @property
    def subarray(self):
        return self._subarray
    
    @subarray.setter
    def subarray(self, value):
        if value is not None and not isinstance(value, Subarray):
            raise ValueError('subarray must be a Subarray instance')
        self._subarray = value

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError('meta must be a dict instance')
        self._meta = value
    