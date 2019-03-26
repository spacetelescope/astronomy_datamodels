# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers
import astropy.units as u
import astropy.coordinates as coords
from ..target import Target

def test1(tmpdir):
    coord = coords.FK5(ra=14*u.deg, dec=-7.5*u.deg)
    target = Target(id='NGC 7356', coordinates=coord, name="my future Nobel target",
            aliases=['black hole catalog 7', "Darth Vader's home"],
            meta={'secret':'Top', 'coordinates':"are wrong for security purposes"})    
    tree = {'target': target}
    helpers.assert_roundtrip_tree(tree, tmpdir)