# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers
import astropy.units as u
import astropy.coordinates as coords
from ..spectrum_aperture import SpectrumAperture
from ..telescope import Telescope

def test1(tmpdir, ret=False):
    center = [23.7, 15.2]
    footprint = [[23, 24.4, 24.4, 23], [10.2, 10.2, 20.2, 20.2]]
    spectrum_aperture = SpectrumAperture(center=center, footprint=footprint,
                                         aperture_id='42', meta={'purpose':'background'})
    tree = {'spectrum_aperture': spectrum_aperture}
    if ret:
        return spectrum_aperture
    helpers.assert_roundtrip_tree(tree, tmpdir)
