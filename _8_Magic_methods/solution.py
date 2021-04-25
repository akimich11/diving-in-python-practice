import os
import tempfile


class File:
    def __init__(self, filename):
        try:
            open(filename).close()
        except FileNotFoundError:
            open(filename, "w").close()
        self.filename = filename
        self.file = None

    def read(self):
        with open(self.filename) as f:
            return f.read()

    def write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)
        return len(content)

    def __add__(self, other):
        if isinstance(other, File):
            content = self.read() + other.read()
            filename = tempfile.NamedTemporaryFile().name
            new_file = File(os.path.join(tempfile.gettempdir(), filename))
            new_file.write(content)
            return new_file

    def __iter__(self):
        self.file = open(self.filename)
        return self

    def __next__(self):
        return self.file.__next__()

    def __str__(self):
        return self.filename
