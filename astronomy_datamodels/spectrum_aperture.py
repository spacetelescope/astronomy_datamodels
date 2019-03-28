# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import numpy as np
from .dm_util import check_sequence_type

class SpectrumAperture:

    def __init__(self, center, footprint, aperture_id, meta=None):
        self.center = center
        self.footprint = footprint
        self.aperture_id = aperture_id
        self.meta = meta

    @property
    def center(self):
        return self._center
    
    @center.setter
    def center(self, value):
        if value is None:
            raise ValueError("must supply center coordinates")
        check_sequence_type(value, float, length=2)
        self._center = value
        
    @property
    def footprint(self):
        return self._footprint
    
    @footprint.setter
    def footprint(self, value):
        if value is None:
            raise ValueError("must supply footprint coordinates")
        avalue = np.array(value, dtype=np.float)
        if len(avalue.shape) !=2 and avalue.shape[0] != 2:
            raise ValueError("footprint must be of shape 2xn points")
        self._footprint = avalue

    @property
    def aperture_id(self):
        return self._aperture_id
    
    @aperture_id.setter
    def aperture_id(self, value):
        if not isinstance(value, str) and not isinstance(value, int):
            raise ValueError("aperture_id must be a string or integer")
        self._aperture_id = value
    
    @property
    def meta(self):
        return self._meta
    
    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError("meta must be a dictionary")
        self._meta = value
        
        