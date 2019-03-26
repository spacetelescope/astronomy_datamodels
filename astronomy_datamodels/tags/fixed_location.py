# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..fixed_location import FixedLocation


class FixedLocationType(AstronomyDataModelType):
    name = 'datamodel/fixed_location'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.fixed_location.FixedLocation']
    requires = ["astropy"]

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['solar_system_body'] = node.solar_system_body
        d['latitude'] = yamlutil.custom_tree_to_tagged_tree(node.latitude, ctx)
        d['longitude'] = yamlutil.custom_tree_to_tagged_tree(node.longitude, ctx)
        if node.altitude is not None:
            d['altitude'] = yamlutil.custom_tree_to_tagged_tree(node.altitude, ctx)
        if node.meta is not None:
            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation
        solar_system_body = node['solar_system_body']
        latitude = yamlutil.tagged_tree_to_custom_tree(node['latitude'], ctx)
        longitude = yamlutil.tagged_tree_to_custom_tree(node['longitude'], ctx)
        fixed_location = FixedLocation(latitude=latitude, longitude=longitude, 
                                       solar_system_body=solar_system_body)
        if 'altitude' in node:
            fixed_location.altitude = yamlutil.tagged_tree_to_custom_tree(node['altitude'], ctx)
        if 'meta' in node:
            fixed_location.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'], ctx)
        return fixed_location

    @classmethod
    def assert_equal(cls, old, new):
        pass

