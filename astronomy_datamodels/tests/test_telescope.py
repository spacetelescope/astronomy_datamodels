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
from ..telescope import Telescope

def test1(tmpdir):
    loc = FixedLocation(latitude=coords.Angle(15*u.deg), 
                        longitude=coords.Angle(-7.5*u.deg))
    tel = Telescope(name='VLA', location=loc)
    tree = {'telescope': tel}
    helpers.assert_roundtrip_tree(tree, tmpdir)

def test2(tmpdir):
    loc = FixedLocation(latitude=coords.Angle(15*u.deg), 
                        longitude=coords.Angle(-7.5*u.deg))
    tel = Telescope(name='VLA', location=loc,
                    location_name="Plains of Saint Augustine",
                    telescope_type=['Radio'],
                    org_url='nrao.edu',
                    telescope_url='https://public.nrao.edu/telescopes/vla/',
                    meta={'fines':'hitting cows'})
    tree = {'telescope': tel}
    helpers.assert_roundtrip_tree(tree, tmpdir)
