# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..detector2dCCD import Detector2dCCD


class Detector2dCCDType(AstronomyDataModelType):
    name = 'datamodel/detector2d-ccd'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.detector2d_ccd.Detector2dCCD']
    requires = []

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}

            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation

        detector2dCCD = Detector2dCCD()
        if 'meta' in node:
            prop.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'], ctx)
        return detector2dCCD

    @classmethod
    def assert_equal(cls, old, new):
        pass

