# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..obs_context import ObsContext


class ObsContextType(AstronomyDataModelType):
    name = 'datamodel/obs_context'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.obs_context.ObsContext']
    requires = ["astropy"]

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        if node.telescope is not None:
            d['telescope'] = yamlutil.custom_tree_to_tagged_tree(node.telescope, ctx)
        if node.instrument is not None:
            d['instrument'] = yamlutil.custom_tree_to_tagged_tree(node.instrument, ctx)
        if node.proposal is not None:
            d['proposal'] = yamlutil.custom_tree_to_tagged_tree(node.proposal, ctx)
        if node.observers is not None:
            d['observers'] = yamlutil.custom_tree_to_tagged_tree(node.observers, ctx)
        if node.target is not None:
            d['target'] = yamlutil.custom_tree_to_tagged_tree(node.target, ctx)
        if node.associated_data is not None:
            d['associated_data'] = yamlutil.custom_tree_to_tagged_tree(node.associated_data, ctx)
        if node.meta is not None:
            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation

        obscontext = ObsContext()
        if 'telescope' in node:
            obscontext.telescope = yamlutil.tagged_tree_to_custom_tree(node['telescope'], ctx)
        if 'instrument' in node:
            obscontext.instrument = yamlutil.tagged_tree_to_custom_tree(node['instrument'], ctx)
        if 'proposal' in node:
            obscontext.proposal = yamlutil.tagged_tree_to_custom_tree(node['proposal'], ctx)
        if 'observers' in node:
            obscontext.observers = yamlutil.tagged_tree_to_custom_tree(node['observers'], ctx)
        if 'target' in node:
            obscontext.target = yamlutil.tagged_tree_to_custom_tree(node['target'], ctx)
        if 'associated_data' in node:
            obscontext.associated_data = yamlutil.tagged_tree_to_custom_tree(node['associated_data'], ctx)
        if 'meta' in node:
            obscontext.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'], ctx)
        return obscontext 

    @classmethod
    def assert_equal(cls, old, new):
        pass

