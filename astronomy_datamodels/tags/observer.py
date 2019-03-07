from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..datamodels import Observer


class ObserverType(AstronomyDataModelType):
    name = 'datamodel/observer'
    version = '1.0.0'
    supported_versions = ['1.0.0', AsdfSpec('>=1.1.0')]
    types = ['asdf_astronomy_schemas_python.datamodels.Observer']
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
            d['PI'] = node.PI
        if node.meta is not None:
            d['meta'] = node.meta
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation
        name = node['name']
        obs = Observer(name)
        if 'email' in node:
            obs.email = node['email']
        return obs

    @classmethod
    def assert_equal(cls, old, new):
        pass

