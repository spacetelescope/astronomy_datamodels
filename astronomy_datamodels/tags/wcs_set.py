# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..wcs_set import WcsSet


class WcsSetType(AstronomyDataModelType):
    name = 'datamodel/wcs_set'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.wcs_set.WcsSet']
    requires = ["astropy", "gwcs"]

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['default'] = yamlutil.custom_tree_to_tagged_tree(node.default, ctx)
        extra_keys = node.keys()
        for key in extra_keys:
            d[key] = yamlutil.custom_tree_to_tagged_tree(getattr(node, key), ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation

        wcs_set = WcsSet(yamlutil.tagged_tree_to_custom_tree(node['default'], ctx))
        # need to fill this out!
        return wcs_set

    @classmethod
    def assert_equal(cls, old, new):
        pass

