# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import pytest
import numpy as np

asdf = pytest.importorskip('asdf', minversion='2.0.0.dev0')
from asdf import util
from asdf.tests import helpers
import gwcs
from gwcs import coordinate_frames as cf
from astropy.modeling import models
from astropy import units as u
from astropy import coordinates as coords
from ..wcs_set import WcsSet


def test1(tmpdir):
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
    tree = {'wcs_set': WcsSet(default=wcsobj, extra=wcsobj)}
    helpers.assert_roundtrip_tree(tree, tmpdir)
