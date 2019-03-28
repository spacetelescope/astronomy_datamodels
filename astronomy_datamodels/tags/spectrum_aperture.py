# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..spectrum_aperture import SpectrumAperture
import numpy as np


class SpectrumApertureType(AstronomyDataModelType):
    name = 'datamodel/spectrum_aperture'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.spectrum_aperture.SpectrumAperture']
    requires = []

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['center'] = yamlutil.custom_tree_to_tagged_tree(node.center, ctx)
        d['footprint'] = yamlutil.custom_tree_to_tagged_tree(node.footprint, ctx)
        d['aperture_id'] = node.aperture_id
        if node.meta is not None:
            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta, ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation

        center = yamlutil.tagged_tree_to_custom_tree(node['center'], ctx)
        footprint = yamlutil.tagged_tree_to_custom_tree(node['footprint'], ctx)
        aperture_id = node['aperture_id']
        spectrum_aperture = SpectrumAperture(center=center, footprint=footprint,
                                              aperture_id=aperture_id)
        if 'meta' in node:
            spectrum_aperture.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'], ctx)
        return spectrum_aperture

    @classmethod
    def assert_equal(cls, old, new):
        pass

