from .reader import Reader
import xml.etree.ElementTree as et

class FDX_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)

    def open(self):
        try:
            self.open_file = et.parse(self.file_name)
            self.content = self.open_file.getroot()[0]
        except Exception as err:
            print('An error ocuured while parsing file \"'+self.file_name+'\"', err)
            exit()

    def read(self):
        try:
            '''
            for child in self.content:
                print(child.tag, child.attrib)
            '''
            pass
        except Exception as err:
            print('Something went wrong with FDX_reader: ', err)
            exit()
        return ''