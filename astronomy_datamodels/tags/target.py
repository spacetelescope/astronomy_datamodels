# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..target import Target


class TargetType(AstronomyDataModelType):
    name = 'datamodel/target'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.target.Target']
    requires = ["astropy"]

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['id'] = node.id
        d['coordinates'] = yamlutil.custom_tree_to_tagged_tree(node.coordinates, ctx)
        if node.name is not None:
            d['name'] = yamlutil.custom_tree_to_tagged_tree(node.name, ctx)
        if node.aliases is not None:
            d['aliases'] = yamlutil.custom_tree_to_tagged_tree(node.aliases, ctx)
        if node.meta is not None:
            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation
        id = node['id']
        coordinates = yamlutil.tagged_tree_to_custom_tree(node['coordinates'], ctx)
        target = Target(id, coordinates=coordinates)
        if 'name' in node:
            target.name = node['name']
        if 'aliases' in node:
            target.aliases = yamlutil.tagged_tree_to_custom_tree(node['aliases'], ctx)
        if 'meta' in node:
            target.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'], ctx)
        return target

    @classmethod
    def assert_equal(cls, old, new):
        pass

