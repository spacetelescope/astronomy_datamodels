# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from dm_util import check_sequence_type
from .subarray import Subarray

class Detector2dCCD:

    def __init__(self, name, size, binning=None, subarray=None,
                 meta=None):
        self.name = name
        check_sequence_type(size, stype=int, length=2)
        self.size = size
        if binning is not None:
            check_sequence_type(binning, stype=int, length=2)
        self.binning = binning
        if subarray is not None:
            self.subarray = subarray
        if meta is not None:
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
        if not isinstance(value, Subarray)

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError('meta must be a dict instance')
        self._meta = value
    