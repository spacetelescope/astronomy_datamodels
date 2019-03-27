# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..telescope import Telescope


class TelescopeType(AstronomyDataModelType):
    name = 'datamodel/telescope'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.telescope.Telescope']
    requires = ["astropy"]

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['name'] = node.name
        d['location'] = yamlutil.custom_tree_to_tagged_tree(node.location, ctx)
        if node.organization is not None:
            d['organization'] = node.organization
        if node.org_url is not None:
            d['org_url'] = node.org_url
        if node.telescope_url is not None:
            d['telescope_url'] = node.telescope_url
        if node.telescope_type is not None:
            d['telescope_type'] = node.telescope_type
        if node.location_name is not None:
            d['location_name'] = node.location_name
        if node.meta is not None:
            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation
        name = node['name']
        location = yamlutil.tagged_tree_to_custom_tree(node['location'], ctx)
        telescope = Telescope(name=name, location=location)
        if 'organization' in node:
            telescope.organization = node['organization']
        if 'org_url' in node:
            telescope.org_url = node['org_url']
        if 'telescope_url' in node:
            telescope.telescope_url = node['telescope_url']
        if 'telescope_type' in node:
            telescope.telescope_type = yamlutil.tagged_tree_to_custom_tree(
                                         node['telescope_type'], ctx)
        if 'location_name' in node:
            telescope.location_name = node['location_name']
        if 'meta' in node:
            telescope.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'], ctx)
        return telescope

    @classmethod
    def assert_equal(cls, old, new):
        pass

