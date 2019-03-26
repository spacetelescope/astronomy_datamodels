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

def test1(tmpdir):
    location = FixedLocation(latitude=coords.Angle(22*u.deg), 
                             longitude=coords.Angle(-7.5*u.deg))
    tree = {'location': location}
    helpers.assert_roundtrip_tree(tree, tmpdir)

def test2(tmpdir):
    location = FixedLocation(solar_system_body='Mars',
                             latitude=coords.Angle(1*u.rad),
                             longitude=coords.Angle(-.7*u.rad),
                             altitude=500*u.m,
                             meta={'message': 'running out of food and oxygen'})
    tree = {'location': location}
    helpers.assert_roundtrip_tree(tree, tmpdir)
