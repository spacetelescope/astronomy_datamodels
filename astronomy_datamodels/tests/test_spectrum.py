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
import gwcs
from gwcs import coordinate_frames as cf
from astropy.modeling import models
from ..fixed_location import FixedLocation
from ..detector2d_ccd import Detector2dCCD
from ..subarray import Subarray
from ..proposal import Proposal 
from ..observer import Observer 
from ..instrument import Instrument 
from ..target import Target
from ..obs_context import ObsContext
from ..telescope import Telescope
from ..spectrum import Spectrum
from ..wcs_set import WcsSet
from .test_obs_context import test1 as oc_test1
from .test_proposal import test1 as pr_test1
from .test_proposal import obs1, obs2
from .test_target import test1 as ta_test1
from .test_instrument import test1 as in_test1
from .test_telescope import test1 as tel_test1
from .test_wcs_set import test1 as wcs_test1
from .test_spectrum_aperture import test1 as sa_test1


import numpy as np

def test1(tmpdir, ret=False):

    spectrum_aperture = sa_test1(None, ret=True)
    wcs_set = wcs_test1(None, ret=True)
    obs_context = oc_test1(None, ret=True)
    sci = np.ones((10,10))*u.Jy
    dq = np.zeros((10,10), dtype= np.int16)
    err = np.ones((10,10))*u.Jy

    spectrum = Spectrum(sci=sci, wcs=wcs_set,dq=dq, err=err,
                        aperture=spectrum_aperture, target_id='NGClown',
                        background_corrected=True, obsinfo=obs_context)
    tree = {'spectrum': spectrum}
    if ret:
        return spectrum
    helpers.assert_roundtrip_tree(tree, tmpdir)