# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from astropy.units import Quantity
from .dm_util import check_sequence_type
from .spectrum import Spectrum


class Mos:

    def __init__(self, fields, field_separator, datasets, meta=None):
        self.fields = fields
        self.field_separator = field_separator
        self.datasets = datasets
        self.meta = meta

    @property
    def fields(self):
        return self._fields
    
    @fields.setter
    def fields(self, value):
        check_sequence_type(value, dict)
        for d in value:
            if 'name' not in d:
                raise ValueError('all fields entries must have a name attribute')
            if not isinstance(d['name'], str):
                raise ValueError('name attribute must be a string')
            if 'data_attribute' in d and not isinstance(d['data_attribute'], str):
                raise ValueError('data_attribute attribute must be a string')
            if 'field_type' in d and d['field_type'] not in ('s', 'i'):
                raise ValueError("field_type attribute must have a value of 's' or 'i'")
        self._fields = value

    @property
    def field_separator(self):
        return self._field_separator
    
    @field_separator.setter
    def field_separator(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("field_separator must be a string")
        self._field_separator = value
        
    @property
    def datasets(self):
        return self._datasets
    
    @datasets.setter
    def datasets(self, value):
        if not isinstance(value, dict):
            raise ValueError("datasets must be a dictionary")
        for key in value:
            if not isinstance(value[key], Spectrum):
                raise ValueError("all dataset dictionary values must be Spectrum instances")
        self._datasets = value

    @property
    def meta(self):
        return self._meta
    
    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError("meta must be a dictionary")
        self._meta = value
        
        