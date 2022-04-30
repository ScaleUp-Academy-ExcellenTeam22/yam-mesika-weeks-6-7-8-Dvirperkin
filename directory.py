import binary_file
import textual_file


class Directory:
    def __init__(self, name, files=None):
        if files is None:
            files = []
        self.name = name
        self.files = files

