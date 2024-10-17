import xml.etree.ElementTree as et
from reader import Reader

class FDX_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)

    def open(self):
        self.open_file = et.parse(self.file_name)
        self.root = self.open_file.getroot()

    def read(self):
        pass