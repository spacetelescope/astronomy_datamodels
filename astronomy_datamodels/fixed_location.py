# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from astropy import units
from astropy.coordinates import Angle
from .dm_util import check_sequence_type

ALLOWABLE_SOLAR_SYSTEM_BODIES = (
     "Earth",
     "Moon",
     "Mercury",
     "Venus",
     "Mars",
     "Io",
     "Europa",
     "Ganymede",
     "Callisto",
     "Mimas",
     "Enceladus",
     "Tethys",
     "Dione",
     "Rhea",
     "Titan",
     "Hyperion",
     "Iapetus",
     "Phoebe",
     "Ariel",
     "Umbriel",
     "Titania",
     "Oberon",
     "Miranda",
     "Triton",
     "Nereid",
     "Proteus",
     "Charon",
     "Vesta",
     "Ceres",
     "Pallas",
     "Hygie"
)

class FixedLocation:

    solar_system_bodies = ALLOWABLE_SOLAR_SYSTEM_BODIES 

    def __init__(self,  latitude, 
                 longitude, altitude=None, solar_system_body=None, meta=None):
        self.solar_system_body = solar_system_body
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.meta = meta

    @property
    def solar_system_body(self):
        return self._solar_system_body
    
    @solar_system_body.setter
    def solar_system_body(self, value):
        if value is not None and value not in ALLOWABLE_SOLAR_SYSTEM_BODIES:
            raise ValueError("solar_system_body must be in the permitted list.")
                        
        if value is None:
            value = "Earth"
        self._solar_system_body = value

    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, Angle):
            raise ValueError("latitude must be an astropy angle")
        self._latitude = value
        
    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, value):
        if value is not None and not isinstance(value, Angle):
            raise ValueError("longitude must be an astropy angle")
        self._longitude = value
        
    @property
    def altitude(self):
        return self._altitude
    
    @altitude.setter
    def altitude(self, value):
        if value is not None and not isinstance(value, units.Quantity):
            raise ValueError("altitude must be an astropy Quantity")
        self._altitude = value
        
    @property
    def meta(self):
        return self._meta
    
    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError("meta must be a dictionary")
        self._meta = value
        