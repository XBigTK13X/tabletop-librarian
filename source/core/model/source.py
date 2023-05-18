class Source:
    def __init__(self, conf):
        self.name = conf['Name']
        self.id = conf['Id']
        self.location = conf['Location']
        self.kind  = conf['Kind']
        self.content = conf['Content']