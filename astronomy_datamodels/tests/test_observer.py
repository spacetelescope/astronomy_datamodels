# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers

from  ..observer import Observer

def test1(tmpdir, ret=False):
    obs = Observer(name='Dummy Name Jr.',
                   institution='Harvaard',
                   address='Harvard Square, Cambridge, MA 02121',
                   email='dname@harvaard.edu',
                   PI=True,
                   meta={'drink_of_choice': 'hemlock',
                         'students': ['Peter', 'Paul', 'Mary']})
    tree = {'observer': obs}
    if ret:
        return obs
    helpers.assert_roundtrip_tree(tree, tmpdir)