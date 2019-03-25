# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers

from ..subarray import Subarray
from ..detector2d_ccd import Detector2dCCD

def test1(tmpdir):
    subarray = Subarray(name='SA1', offset=(100, 131), size=(100,200))
    detector = Detector2dCCD('CCD1', size=(2048, 2048), binning=(2,2),
                             subarray=subarray)
    tree = {'detector': detector}
    helpers.assert_roundtrip_tree(tree, tmpdir)