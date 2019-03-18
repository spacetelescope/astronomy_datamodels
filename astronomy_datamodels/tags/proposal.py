from asdf import yamlutil
from asdf.versioning import AsdfSpec
from ..types import AstronomyDataModelType
from ..proposal import Proposal


class ProposalType(AstronomyDataModelType):
    name = 'datamodel/proposal'
    version = '1.0.0'
    supported_versions = ['1.0.0']
    types = ['astronomy_datamodels.proposal.Proposal']
    requires = []

    @classmethod
    def to_tree(cls, node, ctx): # to ASDF representation
        d = {}
        d['proposal_id'] = node.id
        if node.proposers is not None:
            d['proposers'] = yamlutil.custom_tree_to_tagged_tree(node.proposers, ctx)
        if node.title is not None:
            d['proposal_title'] = node.title
        if node.meta is not None:
            d['meta'] = yamlutil.custom_tree_to_tagged_tree(node.meta. ctx)
        return d

    @classmethod
    def from_tree(cls, node, ctx): # from ASDF to object representation
        id = node['proposal_id']
        prop = Proposal(id)
        if 'proposers' in node:
            prop.proposers = yamlutil.tagged_tree_to_custom_tree(node['proposers'], ctx)
        if 'proposal_title' in node:
            prop.title = node['proposal_title']
        if 'meta' in node:
            prop.meta = yamlutil.tagged_tree_to_custom_tree(node['meta'])
        return prop

    @classmethod
    def assert_equal(cls, old, new):
        pass

