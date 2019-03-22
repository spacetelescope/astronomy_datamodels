# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

class Observer:
    def __init__(self, name, institution=None, address=None,
                 email=None, PI=None, meta=None):
        self.name = name
        self.institution = institution
        self.address = address
        self.email = email
        self.isPI = PI
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
    def institution(self):
        return self._institution

    @institution.setter
    def institution(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError('institution must be a string')
        self._institution =  value

    @property
    def address(self):
        return self._address
        
    @address.setter
    def address(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError('address must be a string')
        self._address =  value
    
    @property
    def email(self):
        return self._email
        
    @address.setter
    def email(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError('email must be a string')
        self._email =  value

    @property
    def isPI(self):
        return self._isPI
        
    @isPI.setter
    def isPI(self, value):
        if value is not None and not isinstance(value, bool):
            raise ValueError('PI must be a boolean')
        self._isPI =  value

    @property
    def meta(self):
        return self._meta    

    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError('meta must be a dict instance')
        self._meta = value
