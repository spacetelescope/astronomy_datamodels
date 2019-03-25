# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers
import astropy.units as u
from ..instrument import Instrument
from ..detector2d_ccd import Detector2dCCD
from ..subarray import Subarray

def test1(tmpdir):
    subarray = Subarray(name='SA1', offset=(100, 131), size=(100,200))
    detector = Detector2dCCD('CCD1', size=(2048, 2048), binning=(2,2),
                             subarray=subarray)
    detectors = [detector]
    engineering = {'beertap': 'off', 'background_level': 'heavy metal rock'}
    meta = {'purpose': 'built for thesis', 'funding': 'bake sales'}
    instrument = Instrument(name='The Big Eye', instrument_type="CAMERA",
                             filters=['F480W'], detectors=detectors,
                             spectral_range=[350 * u.nm, 550 * u.nm],
                             mode='full field', meta=meta,
                             engineering=engineering)
    tree = {'instrument': instrument}
    helpers.assert_roundtrip_tree(tree, tmpdir)