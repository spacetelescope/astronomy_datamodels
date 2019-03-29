# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers

from ..observer import Observer
from ..proposal import Proposal

def test1(tmpdir, ret=False):
    obs_buddy = Observer('Marvin')
    obs1 = Observer(name='Dummy Name Jr.',
                   institution='Harvaard',
                   address='Harvard Square, Cambridge, MA 02121',
                   email='dname@harvaard.edu',
                   PI=True,
                   meta={'drink_of_choice': 'hemlock',
                         'students': ['Peter', 'Paul', 'Mary'],
                         'observer_buddy': obs_buddy
                         })
    obs2 = Observer(name='Bozo the Clown')
    prop = Proposal(327, proposers=[obs1, obs2])
    tree = {'proposal': prop}
    helpers.assert_roundtrip_tree(tree, tmpdir)