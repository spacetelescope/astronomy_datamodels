# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from astropy import units
from .dm_util import check_sequence_type
from .telescope import Telescope
from .observer import Observer
from .proposal import Proposal 
from .instrument import Instrument
from .target import Target

class ObsContext:

    def __init__(self, telescope=None, instrument=None,
                       proposal=None, observers=None,
                       target=None, associated_data=None,
                       meta=None):
        self.telescope = telescope
        self.instrument = instrument
        self.proposal = proposal
        self.observers = observers
        self.target = target
        self.associated_data = associated_data
        self.meta = meta

    @property
    def telescope(self):
        return self._telescope
    
    @telescope.setter
    def telescope(self, value):
        if value is not None and not isinstance(value, Telescope):
            raise ValueError("telescope must be a Telescope instance")
        self._telescope = value

    @property
    def instrument(self):
        return self._instrument
    
    @instrument.setter
    def instrument(self, value):
        if value is not None and not isinstance(value, Instrument):
            raise ValueError("instrument must be a Instrument instance")
        self._instrument = value
        
    @property
    def proposal(self):
        return self._proposal
        
    @proposal.setter
    def proposal(self, value):
        if value is not None and not isinstance(value, Proposal):
            raise ValueError("proposal must be a Proposal instance")
        self._proposal = value

    @property
    def observers(self):
        return self._observers
    
    @observers.setter
    def observers(self, value):
        if value is not None:
            check_sequence_type(value, Observer)
        self._observers = value
        
    @property
    def target(self):
        return self._target
    
    @target.setter
    def target(self, value):
        if value is not None and not isinstance(value, Target):
            raise ValueError("target must be a Target instance")
        self._target = value

    @property
    def associated_data(self):
        return self._associated_data
    
    @associated_data.setter
    def associated_data(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError("associated_data must be a dictionary")
        self._associated_data = value

    @property
    def meta(self):
        return self._meta
    
    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError("meta must be a dictionary")
        self._meta = value
        
        
        