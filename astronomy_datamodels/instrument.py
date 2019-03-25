# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from astropy.units import Quantity
from .dm_util import check_sequence_type
from .detector2d_ccd import Detector2dCCD


class Instrument:

    def __init__(self, name, instrument_type,
                 filters=None, disperser=None, spectral_range=None,
                 mode=None, detectors=None, engineering=None,
                 meta=None):
        self.name = name
        self.instrument_type = instrument_type
        self.filters = filters
        self.disperser = disperser
        self.spectral_range = spectral_range
        self.mode = mode
        self.detectors = detectors
        self.engineering = engineering
        self.meta = meta

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None or not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def instrument_type(self):
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, value):
        if value is None or not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._instrument_type = value

    @property
    def filters(self):
        return self._filters

    @filters.setter
    def filters(self, value):
        if value is None:
            raise ValueError("must supply filters used: use ['CLEAR'] if no filter")
        check_sequence_type(value, str)
        self._filters = value

    @property
    def disperser(self):
        return self._disperser

    @disperser.setter
    def disperser(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("disperser must be a string")
        self._disperser = value

    @property
    def spectral_range(self):
        return self._spectral_range

    @spectral_range.setter
    def spectral_range(self, value):
        if value is not None:
            check_sequence_type(value, Quantity, length=2)
        self._spectral_range = value

    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, value):
        if not isinstance(value, str):
            raise ValueError("mode must be a string")
        self._mode = value

    @property
    def detectors(self):
        return self._detectors

    @detectors.setter
    def detectors(self, value):
        if value is None:
            raise ValueError("Must supply one or more detectors in a list or tuple")
        check_sequence_type(value, Detector2dCCD)
        self._detectors = value

    @property
    def engineering(self):
        return self._engineering
    
    @engineering.setter
    def engineering(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError("if supplied, engineering must be a dictionary")
        self._engineering = value

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError("if supplied, meta must be a dictionary")
        self._meta = value


    