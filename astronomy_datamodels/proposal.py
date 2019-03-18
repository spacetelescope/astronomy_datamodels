class Proposal:
    def __init__(self, id, proposers=None, title=None, meta=None):
        self.id = id
        self.proposers = proposers
        self.title = title
        self.meta = meta