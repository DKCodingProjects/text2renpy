from .reader import Reader
import xml.etree.ElementTree as et

class Fdx_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)

    def open(self):
        try:
            self.open_file = et.parse(self.file_name)
            self.content = self.open_file.getroot().find('Content')
            self.curr_index = 0
            self.max_index = len(self.content)
        except Exception as err:
            raise Exception('An error ocuured while parsing file \''+self.file_name+'\' ('+f"{type(err).__name__}: {err}"+')')
    
    def processxml(self):
        pass

    def readline(self) -> tuple[str, dict]:
        try:
            curr_text = ''
            curr_attribs = None
            if self.curr_index < self.max_index:
                if self.content[self.curr_index].tag == 'Paragraph':
                    curr_paragraph = self.content[self.curr_index]
                    curr_attribs = {k.lower(): v.lower() for k, v in curr_paragraph.attrib.items()}
                    if self.content[self.curr_index].find('Text') is not None:
                        curr_text = curr_paragraph.find('Text').text
                self.curr_index += 1
        except Exception as err:
            raise Exception('Something went wrong with Fdx_Reader ('+f"{type(err).__name__}: {err}"+')')
        return curr_text, curr_attribs