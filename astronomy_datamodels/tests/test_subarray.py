# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers
from ..subarray import Subarray

def test1(tmpdir, ret=False):
    subarray = Subarray(offset=(100, 131), size=(256, 256), name='SA1')
    tree = {'subarray': subarray}
    if ret:
        return subarray
    helpers.assert_roundtrip_tree(tree, tmpdir)