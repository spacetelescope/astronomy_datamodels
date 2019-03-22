# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..subarray import Subarray

class SubarrayType(AstronomyDataModelType):
    name = 'datamodel/subarray'
    version = '1.0.0'
    supported_version = ['1.0.0']
    types = ['astronomy_datamodels.subarray.Subarray']
    requires = []

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['offset'] = node.offset
        d['size'] = node.size
        if node.name is not None:
            d['proposers'] = node.name
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation
        offset = node['offset']
        size = node['size']
        sarray = Subarray(offset, size)
        if 'name' in node:
            sarray.name = node['name']
        return sarray
        
    @classmethod
    def assert_equal(cls, old, new):
        pass

