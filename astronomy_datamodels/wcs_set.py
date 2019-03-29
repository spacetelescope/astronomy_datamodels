# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from astropy import units
from .dm_util import check_sequence_type
from .fixed_location import FixedLocation 
import gwcs

class WcsSet:

    def __init__(self, default, **kw):
        if not isinstance(default, gwcs.wcs.WCS):
            raise ValueError("default must be a gwcs WCS instance")
        self.__dict__["default"] = default
        self.__dict__["_others"] = {}
        for key in kw:
            if not isinstance(kw[key], gwcs.wcs.WCS):
                raise ValueError("all keyword arguments must be WCS instances")
            self.__dict__["_others"][key] = kw[key]

    def __getattr__(self, attr):
        if attr == 'default':
            return self.default
        if attr in self._others:
            return self._others[attr]
        else:
            raise AttributeError("attribute {} not found".format(attr))

    def __setattr__(self, attr, value):
        if not isinstance(value, gwcs.wcs.WCS):
            raise ValueError("Value must be an instance of WCS")
        self.__dict__["_others"][attr] = value

    def keys(self):
        return ('default',) + tuple(self._others.keys())