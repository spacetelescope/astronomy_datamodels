# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..xxxtype import Xxxtype


class XxxtypeType(AstronomyDataModelType):
    name = 'datamodel/xxxtype'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.xxxtype.Xxxtype']
    requires = []

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}

            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation

        xxxtype = Xxxtype()
        if 'meta' in node:
            prop.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'], ctx)
        return xxxtype

    @classmethod
    def assert_equal(cls, old, new):
        pass

