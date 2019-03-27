# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from astropy import units
from .dm_util import check_sequence_type
from .fixed_location import FixedLocation 

ALLOWED_TELESCOPE_TYPES = (
    "Radio"
    "Microwave"
    "Millimeter"
    "IR"
    "Visible"
    "UV"
    "X-Ray"
    "Gamma-Ray"
    "Gravitational"
    )

class Telescope:

    allowed_types = ALLOWED_TELESCOPE_TYPES

    def __init__(self, name, location, organization=None, org_url=None,
                 telescope_url=None, telescope_type=None, 
                 location_name=None, meta=None):
        self.name = name
        self.organization = organization
        self.org_url = org_url
        self.telescope_url = telescope_url
        self.telescope_type = telescope_type
        self.location_name = location_name
        self.location = location
        self.meta = meta

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        self._name = value
        
    @property
    def organization(self):
        return self._organization
    
    @organization.setter
    def organization(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("organization must be a string")
        self._organization = value
        
    @property
    def org_url(self):
        return self._org_url
    
    @org_url.setter
    def org_url(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("org_url must be a string")
        self._org_url = value
        
    @property
    def telescope_url(self):
        return self._telescope_url
    
    @telescope_url.setter
    def telescope_url(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("telescope_url must be a string")
        self._telescope_url = value
        
    @property
    def telescope_type(self):
        return self._telescope_type
    
    @telescope_type.setter
    def telescope_type(self, value):
        # if value is not None:
        #     check_sequence_type(value, str)
        #     for item in value:
        #         if item not in ALLOWED_TELESCOPE_TYPES:
        #             raise ValueError("telescope types must be one of Telescope.allowed_types")
        self._telescope_type = value

    @property
    def location_name(self):
        return self._location_name
    
    @location_name.setter
    def location_name(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("location_name must be a string")
        self._location_name = value
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        if not isinstance(value, FixedLocation):
            raise ValueError("location must be a Location object")
        self._location = value
        
    @property
    def meta(self):
        return self._meta
    
    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError("meta must be a dictionary")
        self._meta = value
        
        