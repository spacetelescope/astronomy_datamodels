from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..observer import Observer


class ObserverType(AstronomyDataModelType):
    name = 'datamodel/observer'
    version = '1.0.0'
    supported_versions = ['1.0.0', AsdfSpec('>=1.1.0')]
    types = ['astronomy_datamodels.observer.Observer']
    requires = []

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['name'] = node.name
        if node.institution is not None:
            d['institution'] = node.institution
        if node.address is not None:
            d['address'] = node.address
        if node.email is not None:
            d['email'] = node.email
        if node.isPI is not None:
            d['PI'] = node.isPI
        if node.meta is not None:
            d['meta'] = node.meta
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation
        name = node['name']
        obs = Observer(name)
        if 'email' in node:
            obs.email = node['email']
        if 'address' in node:
            obs.address = node['address']
        if 'institution' in node:
            obs.institution = node['institution'] 
        if 'PI' in node:
            obs.isPI = node['PI']
        if 'meta' in node:
            obs.meta = node['meta']
        return obs

    @classmethod
    def assert_equal(cls, old, new):
        pass

