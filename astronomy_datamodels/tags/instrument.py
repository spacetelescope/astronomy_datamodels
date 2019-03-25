# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..instrument import Instrument


class InstrumentType(AstronomyDataModelType):
    name = 'datamodel/instrument'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.instrument.Instrument']
    requires = ["astropy"]

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['name'] = node.name
        d['instrument_type'] = node.instrument_type
        d['filters'] = yamlutil.custom_tree_to_tagged_tree(node.filters, ctx)
        d['mode'] = yamlutil.custom_tree_to_tagged_tree(node.mode, ctx)
        d['detectors'] = yamlutil.custom_tree_to_tagged_tree(node.detectors, ctx)
        if node.disperser is not None:
            d['disperser'] = node.disperser
        if node.spectral_range is not None:
            d['spectral_range'] = yamlutil.custom_tree_to_tagged_tree(node.spectral_range, ctx)
        if node.engineering is not None:
            d['engineering'] = yamlutil.custom_tree_to_tagged_tree(node.engineering, ctx)
        if node.meta is not None:
            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation
        name = node['name']
        instrument_type = node['instrument_type']
        filters = yamlutil.tagged_tree_to_custom_tree(node['filters'], ctx)
        mode = yamlutil.tagged_tree_to_custom_tree(node['mode'], ctx)
        detectors = yamlutil.tagged_tree_to_custom_tree(node['detectors'], ctx)
        instrument = Instrument(name, instrument_type=instrument_type, filters=filters,
                                mode=mode, detectors=detectors)
        if 'disperser' in node:
            instrument.detector = node['disperser']
        if 'spectral_range' in node:
            instrument.spectral_range = node['spectral_range']
        if 'engineering' in node:
            instrument.engineering = node['engineering']
        if 'meta' in node:
            instrument.meta = node['meta']
        return instrument
        


    @classmethod
    def assert_equal(cls, old, new):
        pass

