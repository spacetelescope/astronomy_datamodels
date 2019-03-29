# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers
from ..mos import Mos
from .test_spectrum import test1 as spec_test1
import numpy as np

def test1(tmpdir, ret=False):
    fields = [{"name":"slit", "data_attribute":"xxx", "field_type":"s"},
              {"name":"visit", "data_attribute":"xxx", "field_type":"i"}]
    field_separator = "|"
    spectrum = spec_test1(None, ret=True)
    datasets = {
        "slit_1|7": spectrum,
        "slit_2|7": spectrum,
        "slit_1|12": spectrum,
        "slit_2|12": spectrum
    }
    mos = Mos(fields=fields, field_separator=field_separator, datasets=datasets)
    tree = {'mos': mos}
    if ret:
        return mos
    helpers.assert_roundtrip_tree(tree, tmpdir)