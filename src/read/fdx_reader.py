from .reader import Reader
from src.misc.text_chunk_data import Text_Chunk_Data
import xml.etree.ElementTree as et

class Fdx_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)

    def lowercase_dict(self, dict):
        return super().lowercase_dict(dict)

    def open(self):
        try:
            self.open_file = et.parse(self.file_name)
            self.content = self.open_file.getroot().find('Content')
            self.curr_index = 0
            self.max_index = len(self.content)
        except Exception as err:
            raise Exception('An error ocuured while parsing file \''+self.file_name+'\' ('+f"{type(err).__name__}: {err}"+')')

    def readpart(self) -> tuple[list[Text_Chunk_Data], dict]:
        try:
            curr_text = []
            curr_attrib = None
            if self.curr_index < self.max_index:
                if self.content[self.curr_index].tag == 'Paragraph':
                    curr_paragraph = self.content[self.curr_index]
                    curr_attrib = self.lowercase_dict(curr_paragraph.attrib)
                    if self.content[self.curr_index].find('Text') is not None:
                        para_len = len(curr_paragraph)
                        para_index = 0
                        while para_index < para_len:
                            if curr_paragraph[para_index].tag == 'Text':
                                para_text = curr_paragraph[para_index]
                                # pass styling to the Text_Chunk_Data object!
                                curr_text.append(Text_Chunk_Data(para_text.text))
                            para_index += 1
                self.curr_index += 1
            else:
                self.is_eof = True
        except Exception as err:
            raise Exception('Something went wrong with Fdx_Reader in method \'readpart\'('+f"{type(err).__name__}: {err}"+')')
        return curr_text, curr_attrib