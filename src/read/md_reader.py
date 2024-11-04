from .reader import Reader
from src.store.text_chunk import Text_Chunk
from src.store.para_attribs import *

class Markdown_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)
    
    def open_except(self, err):
        return super().open_except(err)
    
    def open(self):
        try:
            self.open_file = open(self.file_name, 'r')
        except Exception as err:
            self.open_except(err)
    
    def find_styling(line: str) -> Text_Chunk:
        pass

    def find_chunks(line: str) -> list[Text_Chunk]:
        pass
    
    def readpart_except(self, err):
        return super().readpart_except(err)

    def readpart(self) -> tuple[list[Text_Chunk], Paragraph_Attributes]:
        try:
            text_chunks: list[Text_Chunk] = [Text_Chunk(self.open_file.readline())]
            if text_chunks[0].get_text() == '':
                self.is_eof = True
        except Exception as err:
            self.readpart_except(err)
        return text_chunks, Paragraph_Attributes()