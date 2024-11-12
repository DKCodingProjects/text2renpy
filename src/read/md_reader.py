from .reader import Reader
from src.store.text_chunk import Text_Chunk
from src.store.para_attribs import *

class Markdown_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)
    
    def _open_except(self, err):
        return super()._open_except(err)
    
    def open(self):
        try:
            raise TypeError('class method \'open\' in {0} is still being developed! Update to latest version or wait for a working release!'.format(self.__class__.__name__))
            self.open_file = open(self.file_name, 'r')
        except Exception as err:
            self._open_except(err)
    
    def find_styling(line: str) -> Text_Chunk:
        pass

    def find_chunks(line: str) -> list[Text_Chunk]:
        pass
    
    def _readpart_except(self, err):
        return super()._readpart_except(err)

    def readpart(self) -> tuple[list[Text_Chunk], Paragraph_Attributes]:
        try:
            raise TypeError('class method \'readpart\' in {0} is still being developed! Update to latest version or wait for a working release!'.format(self.__class__.__name__))
            text_chunks: list[Text_Chunk] = [Text_Chunk(self.open_file.readline())]
            if text_chunks[0].get_text() == '':
                self.is_eof = True
        except Exception as err:
            self._readpart_except(err)
        return text_chunks, Paragraph_Attributes()