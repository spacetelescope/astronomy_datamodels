# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import numpy as np
from .dm_util import check_sequence_type, convert_to_array, check_quantity_array
from astropy.units import Quantity
from .wcs_set import WcsSet
from .obs_context import ObsContext
from .spectrum_aperture  import SpectrumAperture

class Spectrum:

    def __init__(self, sci, wcs, dq=None, err=None, aperture=None,
                       target_id=None, background_corrected=None,
                       background_apertures=None, obsinfo=None,
                       meta=None):
        self.sci = sci
        self.wcs = wcs
        self.dq = dq
        self.err = err
        self.aperture = aperture
        self.target_id = target_id
        self.background_corrected = background_corrected
        self.background_apertures = background_apertures
        self.obsinfo = obsinfo
        self.meta = meta

    @property
    def sci(self):
        return self._sci
    
    @sci.setter
    def sci(self, value):
        check_quantity_array(value)
        self._sci = value

    @property
    def wcs(self):
        return self._wcs
    
    @wcs.setter
    def wcs(self, value):
        if not isinstance(value, WcsSet):
            raise ValueError("wcs must be a xxx")
        self._wcs = value

    @property
    def dq(self):
        return self._dq
    
    @dq.setter
    def dq(self, value):
        if value is not None:
            value = convert_to_array(value)
        self._dq = value
        
    @property
    def err(self):
        return self._err
    
    @err.setter
    def err(self, value):
        if value is not None:
            check_quantity_array(value)
        self._err = value
        
    @property
    def aperture(self):
        return self._aperture
    
    @aperture.setter
    def aperture(self, value):
        if value is not None and not isinstance(value, SpectrumAperture):
            raise ValueError("aperture must be a SpectrumAperture instance")
        self._aperture = value
        
    @property
    def background_corrected(self):
        return self._background_corrected
    
    @background_corrected.setter
    def background_corrected(self, value):
        if value is not None and not isinstance(value, bool):
            raise ValueError("background_corrected must be a boolean")
        self._background_corrected = value

    @property
    def background_apertures(self):
        return self._background_apertures
    
    @background_apertures.setter
    def background_apertures(self, value):
        check_sequence_type(value, (str, int))
        self._background_apertures = value

    @property
    def obsinfo(self):
        return self._obsinfo
    
    @obsinfo.setter
    def obsinfo(self, value):
        if value is not None and not isinstance(value, ObsContext):
            raise ValueError("obsinfo must be a ObsContext instance")
        self._obsinfo = value
                    
    @property
    def meta(self):
        return self._meta
    
    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError("meta must be a dictionary")
        self._meta = value
        