# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from astropy import units
from astropy.coordinates import (ICRS, FK4, FK4NoETerms, FK5, Galactic, 
         Galactocentric, GCRS, ITRS, PrecessedGeocentric)
from .dm_util import check_sequence_type

ALLOWED_FRAMES = (ICRS, FK4, FK4NoETerms, FK5, Galactic,
    Galactocentric, GCRS, ITRS, PrecessedGeocentric)

class Target:

    def __init__(self, id, coordinates, name=None, aliases=None, meta=None):
        self.id = id
        self.coordinates = coordinates
        self.name = name
        self.aliases = aliases
        self.meta = meta

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("id must be a string")
        self._id = value
    
    @property
    def coordinates(self):
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self, value):
        if value is not None and not type(value) in ALLOWED_FRAMES:
            raise ValueError("coordinates must be an instance of:\n"
                              "ICRS, FK4, FK4NoETerms, FK5, Galactic,"
                              "Galactocentric,\nGCRS, ITRS, PrecessedGeocentric")
        self._coordinates = value
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("name must be a string")
        self._name = value
        
    @property
    def aliases(self):
        return self._aliases
    
    @aliases.setter
    def aliases(self, value):
        if value is not None:
            check_sequence_type(value, str)
        self._aliases = value

    @property
    def meta(self):
        return self._meta
    
    @meta.setter
    def meta(self, value):
        if value is not None:
            check_sequence_type(value, str)
        self._meta = value
        
        