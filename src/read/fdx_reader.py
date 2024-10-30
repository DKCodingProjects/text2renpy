from .reader import Reader
from src.misc.text_chunk import Text_Chunk
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
        
    def build_chunk(chunk) -> Text_Chunk:
        chunk_data = Text_Chunk(chunk.text)
        chunk_attribs = chunk.attrib
        if 'Style' in chunk_attribs:
            chunk_styles = chunk_attribs['Style'].split('+')
            chunk_data.set_bold(True if ('Bold' in chunk_styles) else False)
            chunk_data.set_italic(True if ('Italic' in chunk_styles) else False)
            chunk_data.set_underline(True if ('Underline' in chunk_styles) else False)
        return chunk_data
    
    def find_chunks(paragraph) -> list[Text_Chunk]:
        text_chunks = []
        para_len = len(paragraph)
        para_index = 0
        while para_index < para_len:
            curr_chunk = paragraph[para_index]
            if curr_chunk.tag == 'Text':
                text_chunks.append(Fdx_Reader.build_chunk(curr_chunk))
            para_index += 1
        return text_chunks

    def readpart(self) -> tuple[list[Text_Chunk], dict]:
        try:
            text_chunks = []
            curr_attrib = None
            if self.curr_index < self.max_index:
                if self.content[self.curr_index].tag == 'Paragraph':
                    curr_paragraph = self.content[self.curr_index]
                    curr_attrib = self.lowercase_dict(curr_paragraph.attrib)
                    if self.content[self.curr_index].find('Text') is not None:
                        text_chunks = Fdx_Reader.find_chunks(curr_paragraph)
                self.curr_index += 1
            else:
                self.is_eof = True
        except Exception as err:
            raise Exception('Something went wrong with Fdx_Reader in method \'readpart\'('+f"{type(err).__name__}: {err}"+')')
        return text_chunks, curr_attrib