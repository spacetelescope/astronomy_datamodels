# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers
import astropy.units as u
import astropy.coordinates as coords
from ..fixed_location import FixedLocation
from ..detector2d_ccd import Detector2dCCD
from ..subarray import Subarray
from ..proposal import Proposal 
from ..observer import Observer 
from ..instrument import Instrument 
from ..target import Target
from ..obs_context import ObsContext
from .test_proposal import test1 as pr_test1
from .test_proposal import obs1, obs2
from .test_target import test1 as ta_test1
from .test_instrument import test1 as in_test1
from .test_telescope import test1 as tel_test1

from ..telescope import Telescope

def test1(tmpdir, ret=False):

    prop = pr_test1(None, ret=True)
    coord = coords.FK5(ra=14*u.deg, dec=-7.5*u.deg)    
    target = ta_test1(None, ret=True)
    instrument = in_test1(None, ret=True)
    tel = tel_test1(None, ret=True)
    obscontext = ObsContext(telescope=tel, instrument=instrument,
                            proposal=prop, observers=[obs1, obs2],
                            target=target, meta={'purpose':'travel'})
    tree = {'obs_context': obscontext}
    if ret:
        return obscontext
    helpers.assert_roundtrip_tree(tree, tmpdir)
