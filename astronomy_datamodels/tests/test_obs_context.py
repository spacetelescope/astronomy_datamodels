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

from ..telescope import Telescope

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
    coord = coords.FK5(ra=14*u.deg, dec=-7.5*u.deg)
    target = Target(id='NGC 7356', coordinates=coord, name="my future Nobel target",
            aliases=['black hole catalog 7', "Darth Vader's home"],
            meta={'secret':'Top', 'coordinates':"are wrong for security purposes"})    
    subarray = Subarray(name='SA1', offset=(100, 131), size=(100,200))
    detector = Detector2dCCD('CCD1', size=(2048, 2048), binning=(2,2),
                                 subarray=subarray)
    meta = {'purpose': 'built for thesis', 'funding': 'bake sales'}
    engineering = {'beertap': 'off', 'background_level': 'heavy metal rock'}
    instrument = Instrument(name='The Big Eye', instrument_type="CAMERA",
                             filters=['F480W'], detectors=[detector],
                             spectral_range=[350 * u.nm, 550 * u.nm],
                             mode='full field', meta=meta,
                             engineering=engineering)

    loc = FixedLocation(latitude=coords.Angle(15*u.deg), 
                        longitude=coords.Angle(-7.5*u.deg))
    tel = Telescope(name='VLA', location=loc)
    obscontext = ObsContext(telescope=tel, instrument=instrument,
                            proposal=prop, observers=[obs1, obs2],
                            target=target, meta={'purpose':'travel'})
    tree = {'obs_context': obscontext}
    if ret:
        return obscontext
    helpers.assert_roundtrip_tree(tree, tmpdir)
