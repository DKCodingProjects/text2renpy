from .reader import Reader
import xml.etree.ElementTree as et
from src.collect.text_chunk import Text_Chunk
from src.collect.para_attribs import *

class Fdx_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)

    def lowercase_dict(self, dict):
        return super().lowercase_dict(dict)

    def open_except(self, err):
        return super().open_except(err)
    
    def open(self):
        try:
            self.open_file = et.parse(self.file_name)
            self.content = self.open_file.getroot().find('Content')
            self.curr_index = 0
            self.max_index = len(self.content)
        except Exception as err:
            self.open_except(err)
    
    def build_attributes(paragraph: et.Element) -> Paragraph_Attributes:
        para_attrib = Paragraph_Attributes()
        attrib_dict = paragraph.attrib
        align_dict = {'Left': 1, 'Center': 2, 'Right': 3}
        para_attrib.set_alignment(Paragraph_Alignment(align_dict[attrib_dict['Alignment']] if ('Alignment' in attrib_dict) else 0))
        para_attrib.set_type(attrib_dict['Type'].lower() if ('Type' in attrib_dict) else None)
        return para_attrib
        
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
        para_index = 0
        para_len = len(paragraph)
        while para_index < para_len:
            curr_chunk = paragraph[para_index]
            if curr_chunk.tag == 'Text':
                text_chunks.append(Fdx_Reader.build_chunk(curr_chunk))
            para_index += 1
        return text_chunks
    
    def readpart_except(self, err):
        return super().readpart_except(err)

    def readpart(self) -> tuple[list[Text_Chunk], dict]:
        try:
            text_chunks: list[Text_Chunk] = []
            para_attribs: Paragraph_Attributes = None
            if self.curr_index < self.max_index:
                if self.content[self.curr_index].tag == 'Paragraph':
                    curr_paragraph = self.content[self.curr_index]
                    para_attribs = Fdx_Reader.build_attributes(curr_paragraph)
                    if curr_paragraph.find('Text') is not None:
                        text_chunks = Fdx_Reader.find_chunks(curr_paragraph)
                self.curr_index += 1
            else:
                self.is_eof = True
        except Exception as err:
            self.readpart_except(err)
        return text_chunks, para_attribs