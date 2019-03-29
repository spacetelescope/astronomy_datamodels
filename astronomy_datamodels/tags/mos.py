# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..mos import Mos


class MosType(AstronomyDataModelType):
    name = 'datamodel/mos'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.mos.Mos']
    requires = ["astropy"]

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['fields'] = yamlutil.custom_tree_to_tagged_tree(node.fields, ctx)
        d['field_separator'] = node.field_separator
        d['datasets'] = yamlutil.custom_tree_to_tagged_tree(node.datasets, ctx)
        if node.meta is not None:
            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation
        fields = yamlutil.tagged_tree_to_custom_tree(node['fields'], ctx)
        field_separator = node['field_separator']
        datasets = yamlutil.tagged_tree_to_custom_tree(node['datasets'], ctx)
        mos = Mos(fields=fields, field_separator=field_separator, datasets=datasets)
        if 'meta' in node:
            mos.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'], ctx)
        return mos

    @classmethod
    def assert_equal(cls, old, new):
        pass

