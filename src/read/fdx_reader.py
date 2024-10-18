from .reader import Reader
import xml.etree.ElementTree as et

class FDX_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)

    def open(self):
        try:
            self.open_file = et.parse(self.file_name)
            self.root = self.open_file.getroot()
        except:
            print('An error ocuured while parsing file \"'+self.file_name+'\"')

    def read(self):
        try:
            pass
        except Exception as e:
            print('Something went wrong with FDX_reader: ', e)
        return ''