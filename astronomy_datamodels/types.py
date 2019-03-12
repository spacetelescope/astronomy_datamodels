# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from asdf.asdftypes import CustomType, ExtensionTypeMeta


__all__ = ['AstronomyDataModelType', 'AstronomyDataModelAsdfType']


_astronomy_datamodel_types = set()
_astronomy_datamodel_asdf_types = set()


class AstronomyDataModelTypeMeta(ExtensionTypeMeta):
    """
    Keeps track of `AstropyType` subclasses that are created so that they can
    be stored automatically by astropy extensions for ASDF.
    """
    def __new__(mcls, name, bases, attrs):
        cls = super().__new__(mcls, name, bases, attrs)
        # Classes using this metaclass are automatically added to the list of
        # astropy extensions
        if cls.standard == 'astronomy_datamodel':
            _astronomy_datamodel_types.add(cls)
        elif cls.standard == 'asdf':
            _astronomy_datamodel_asdf_types.add(cls)

        return cls


class AstronomyDataModelType(CustomType, metaclass=AstronomyDataModelTypeMeta):
    """
    This class represents types that have schemas and tags that are defined by
    Astropy.

    IMPORTANT: This parent class should **not** be used for types that have
    schemas that are defined by the ASDF standard.
    """
    organization = 'astroasdf.org'
    standard = 'astronomy_datamodel'


class AstronomyDataModelAsdfType(CustomType, metaclass=AstronomyDataModelTypeMeta):
    """
    This class represents types that have schemas that are defined in the ASDF
    standard, but have tags that are implemented within astropy.

    IMPORTANT: This parent class should **not** be used for types that also
    have schemas that are defined by astropy.
    """
    organization = 'stsci.edu'
    standard = 'asdf'
