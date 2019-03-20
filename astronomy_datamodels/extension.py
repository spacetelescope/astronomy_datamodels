# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

import os

from asdf.extension import AsdfExtension, BuiltinExtension
from asdf.resolver import Resolver, DEFAULT_URL_MAPPING
from asdf.util import filepath_to_url

# Make sure that all tag implementations are imported by the time we create
# the extension class so that _astropy_asdf_types is populated correctly. We
# could do this using __init__ files, except it causes pytest import errors in
# the case that asdf is not installed.

# from .tags.coordinates.angle import *
# from .tags.coordinates.representation import *
# from .tags.coordinates.frames import *
# from .tags.fits.fits import *
# from .tags.table.table import *
# from .tags.time.time import *
# from .tags.transform.basic import *
# from .tags.transform.compound import *
# from .tags.transform.polynomial import *
# from .tags.transform.projections import *
# from .tags.transform.tabular import *
# from .tags.unit.quantity import *
# from .tags.unit.unit import *
# from .tags.meta import *
from .tags.proposal import *
from .tags.observer import *
from .types import _astronomy_datamodel_types, _astronomy_datamodel_asdf_types


__all__ = ['AstronomyDataModelExtension', 'AstronomyDataModelAsdfExtension']


ASTRONOMY_DATAMODEL_SCHEMA_URI_BASE = 'http://astroasdf.org/astronomy_datamodel/'
SCHEMA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'asdf_astronomy_schemas/schemas'))
ASTRONOMY_DATAMODEL_URL_MAPPING = [
    (ASTRONOMY_DATAMODEL_SCHEMA_URI_BASE,
     os.path.join(filepath_to_url(
         os.path.join(SCHEMA_PATH, 'astroasdf.org')),
         '{url_suffix}.yaml'))]


# This extension is used to register custom types that have both tags and
# schemas defined by Astropy.
class AstronomyDataModelExtension(AsdfExtension):
    @property
    def types(self):
        return _astronomy_datamodel_types

    @property
    def tag_mapping(self):
        return [('tag:astroasdf.org:astronomy_datamodel',
                 ASTRONOMY_DATAMODEL_SCHEMA_URI_BASE + '{tag_suffix}')]

    @property
    def url_mapping(self):
        return ASTRONOMY_DATAMODEL_URL_MAPPING


# This extension is used to register custom tag types that have schemas defined
# by ASDF, but have tag implementations defined in astropy.
class AstronomyDataModelAsdfExtension(BuiltinExtension):
    @property
    def types(self):
        return _astronomy_datamodel_asdf_types
