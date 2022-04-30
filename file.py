class File:
    def __init__(self, name, kb_size, creator, content=None):
        if content is None:
            content = []
        self.name = name
        self.kb_size = kb_size
        self.content = content
        self.creator = creator

    def read(self, username):
        if username == self.creator:
            return
