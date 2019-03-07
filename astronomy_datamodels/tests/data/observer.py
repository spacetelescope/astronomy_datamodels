import os
import asdf
from asdf import util

class Observer(dict):
    def __init__(idict):
        self._dict = idict

class ObserverType(asdf.CustomType):
    name = 'observer'
    organization = 'stsci.edu'
    version = (1, 0, 0)
    standard = 'custom'
    types = [Observer]

    @classmethod
    def to_tree(cls, node, ctx):
        pass

    @classmethod
    def from_tree(cls, tree, ctx):
        odict = dict()
        odict['name'] = tree['name']
        odict['institution'] = tree.get('institution', None)
        odict['address'] = tree.get('address', None)
        odict['email'] = tree.get('email', None)
        odict['PI'] = tree.get('email', None)
        odict['meta'] tree.get('meta', None)
        return Observer(odict)