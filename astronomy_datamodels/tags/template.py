from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ...types import AstronomyDataModelType

class XxxType(AstronomyDataModelType):
    name = 'datamodel/observer'
    version = '1.0.0'
    supported_versions = ['1.0.0', AsdfSpec('>=1.1.0')]
    types = ['xxx']
    requires = []

    @classmethod
    def to_tree(cls, node, ctx):
        pass

    @classmethod
    def from_tree(cls, node, ctx):
        pass

    @classmethod
    def assert_equal(cls, old, new):
        pass

