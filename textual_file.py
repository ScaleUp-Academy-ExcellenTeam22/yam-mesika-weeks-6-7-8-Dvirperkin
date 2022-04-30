from file import File


class TextualFile(File):
    def count(self, string_to_search):
        count = 0
        lines = self.content
        for line in lines:
            if string_to_search in line:
                count += 1
        return count
