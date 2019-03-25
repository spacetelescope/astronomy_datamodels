# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..detector2d_ccd import Detector2dCCD


class Detector2dCCDType(AstronomyDataModelType):
    name = 'datamodel/detector2d_ccd'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.detector2d_ccd.Detector2dCCD']
    requires = []

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['name'] = node.name
        d['size'] = node.size
        if node.binning is not None:
            d['binning'] = yamlutil.custom_tree_to_tagged_tree(node.binning, ctx)
        if node.subarray is not None:
            d['subarray'] = yamlutil.custom_tree_to_tagged_tree(node.subarray, ctx)
        if node.meta is not None:
            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation
        name = node['name']
        size = node['size']
        detector = Detector2dCCD(name, size)
        if 'binning' in node:
            detector.binning = yamlutil.tagged_tree_to_custom_tree(node['binning'], ctx)
        if 'subarray' in node:
            detector.subarray = yamlutil.tagged_tree_to_custom_tree(node['subarray'], ctx)
        if 'meta' in node:
            detector.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'], ctx)
        return detector

    @classmethod
    def assert_equal(cls, old, new):
        pass

