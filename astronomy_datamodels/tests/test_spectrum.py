# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers
import astropy.units as u
import astropy.coordinates as coords
from ..spectrum_aperture import SpectrumAperture
import astropy.units as u
import astropy.coordinates as coords
import gwcs
from gwcs import coordinate_frames as cf
from astropy.modeling import models
from ..fixed_location import FixedLocation
from ..detector2d_ccd import Detector2dCCD
from ..subarray import Subarray
from ..proposal import Proposal 
from ..observer import Observer 
from ..instrument import Instrument 
from ..target import Target
from ..obs_context import ObsContext
from ..telescope import Telescope
from ..spectrum import Spectrum
from ..wcs_set import WcsSet
import numpy as np

def test1(tmpdir):
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

    center = [23.7, 15.2]
    footprint = [[23, 24.4, 24.4, 23], [10.2, 10.2, 20.2, 20.2]]
    spectrum_aperture = SpectrumAperture(center=center, footprint=footprint,
                                         aperture_id='42', meta={'purpose':'background'})

    shift_by_crpix = models.Shift(-2048*u.pix) & models.Shift(-1024*u.pix)
    matrix = np.array([[1.290551569736E-05, 5.9525007864732E-06],
                       [5.0226382102765E-06 , -1.2644844123757E-05]])
    rotation = models.AffineTransformation2D(matrix * u.deg,
                                            translation=[0, 0] * u.deg)
    rotation.input_units_equivalencies = {"x": u.pixel_scale(1*u.deg/u.pix),
                                          "y": u.pixel_scale(1*u.deg/u.pix)}
    rotation.inverse = models.AffineTransformation2D(np.linalg.inv(matrix) * u.pix,
                                                     translation=[0, 0] * u.pix)
    rotation.inverse.input_units_equivalencies = {"x": u.pixel_scale(1*u.pix/u.deg),
                                                  "y": u.pixel_scale(1*u.pix/u.deg)}
    tan = models.Pix2Sky_TAN()
    celestial_rotation =  models.RotateNative2Celestial(
         5.63056810618*u.deg, -72.05457184279*u.deg, 180*u.deg)
    det2sky = shift_by_crpix | rotation | tan | celestial_rotation
    det2sky.name = "linear_transform"
    detector_frame = cf.Frame2D(name="detector", axes_names=("x", "y"),
                                unit=(u.pix, u.pix))
    sky_frame = cf.CelestialFrame(reference_frame=coords.ICRS(),
                                  name='icrs',
                                  unit=(u.deg, u.deg))
    pipeline = [(detector_frame, det2sky),
                (sky_frame, None)
               ]
    wcsobj = gwcs.wcs.WCS(pipeline)
    wcs_set = WcsSet(default=wcsobj, extra=wcsobj)

    sci = np.ones((10,10))
    dq = np.zeros((10,10), dtype= np.int16)
    err = np.ones((10,10))

    spectrum = Spectrum(sci=sci, wcs=wcs_set,dq=dq, err=err,
                        aperture=spectrum_aperture, target_id='NGClown',
                        background_corrected=True)
    tree = {'spectrum': spectrum}
    helpers.assert_roundtrip_tree(tree, tmpdir)