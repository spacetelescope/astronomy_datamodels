class Observer:
    def __init__(self, name, institution=None, address=None,
                 email=None, PI=None, meta=None):
        self.name = name
        self.institution = institution
        self.address = address
        self.email = email
        self.isPI = PI
        self.meta = meta
