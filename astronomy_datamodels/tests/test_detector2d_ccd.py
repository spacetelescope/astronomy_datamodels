# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers

from ..subarray import Subarray
from ..detector2d_ccd import Detector2dCCD
from .test_subarray import test1 as sa_test1

def test1(tmpdir, ret=False):

    subarray = sa_test1(None, ret=True)
    detector = Detector2dCCD('CCD1', size=(2048, 2048), binning=(2,2),
                             subarray=subarray)
    tree = {'detector': detector}
    if ret:
        return detector
    helpers.assert_roundtrip_tree(tree, tmpdir)