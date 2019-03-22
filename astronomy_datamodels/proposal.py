# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from .observer import Observer
from .dm_util import check_sequence_type

class Proposal:
    def __init__(self, id, proposers=None, title=None, meta=None):
        self.id = id
        self.proposers = proposers
        self.title = title
        self.meta = meta

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, str) and not isinstance(value, int):
            raise ValueError("id must be a string or integer")
        self._id = value

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("title must be a string")
        self._title = value

    @property
    def proposers(self):
        return self._proposers

    @proposers.setter
    def proposers(self, value):
        if value is not None:
            check_sequence_type(value, Observer)
        self._proposers = value
    
    @property
    def meta(self):
        return self._meta
    
    @meta.setter
    def meta(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError('meta must be a dict instance')
        self._meta = value
