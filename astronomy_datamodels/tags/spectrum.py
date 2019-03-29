# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..spectrum import Spectrum


class SpectrumType(AstronomyDataModelType):
    name = 'datamodel/spectrum'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.spectrum.Spectrum']
    requires = ["astropy", "gwcs"]

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['sci'] = yamlutil.custom_tree_to_tagged_tree(node.sci, ctx)
        d['wcs'] = yamlutil.custom_tree_to_tagged_tree(node.wcs, ctx)
        if node.dq is not None:
            d['dq'] = yamlutil.custom_tree_to_tagged_tree(node.dq, ctx)
        if node.err is not None:
            d['err'] = yamlutil.custom_tree_to_tagged_tree(node.err, ctx)
        if node.aperture is not None:
            d['aperture'] = yamlutil.custom_tree_to_tagged_tree(node.aperture, ctx)
        if node.target_id is not None:
            d['target_id'] = yamlutil.custom_tree_to_tagged_tree(node.target_id, ctx)
        if node.background_corrected is not None:
            d['background_corrected'] = yamlutil.custom_tree_to_tagged_tree(node.background_corrected, ctx)
        if node.background_apertures is not None:
            d['background_apertures'] = yamlutil.custom_tree_to_tagged_tree(node.background_apertures, ctx)
        if node.meta is not None:
            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation

        sci = yamlutil.tagged_tree_to_custom_tree(node['sci'], ctx)
        wcs = yamlutil.tagged_tree_to_custom_tree(node['wcs'], ctx)
        spectrum = Spectrum(sci=sci, wcs=wcs)
        if 'dq' in node:
            spectrum.dq = yamlutil.tagged_tree_to_custom_tree(node['dq'], ctx)
        if 'err' in node:
            spectrum.err = yamlutil.tagged_tree_to_custom_tree(node['err'], ctx)
        if 'aperture' in node:
            spectrum.aperture = yamlutil.tagged_tree_to_custom_tree(node['aperture'], ctx)
        if 'target_id' in node:
            spectrum.target_id = yamlutil.tagged_tree_to_custom_tree(node['target_id'], ctx)
        if 'background_corrected' in node:
            spectrum.background_corrected = yamlutil.tagged_tree_to_custom_tree(node['background_corrected'], ctx)
        if 'background_apertures' in node:
            spectrum.background_apertures = yamlutil.tagged_tree_to_custom_tree(node['background_apertures'], ctx)
        if 'meta' in node:
            spectrum.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'], ctx)
        return spectrum

    @classmethod
    def assert_equal(cls, old, new):
        pass

