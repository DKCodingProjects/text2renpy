from .reader import Reader
from src.data.prog.build.text_chunk import Text_Chunk

class Raw_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)
    
    def _open_except(self, err):
        return super()._open_except(err)
    
    def open(self):
        try:
            self.open_file = open(self.file_name, 'r')
        except Exception as err:
            self._open_except(err)
        
    def _readpart_except(self, err):
        return super()._readpart_except(err)

    def readpart(self) -> list[Text_Chunk]:
        try:
            text_chunks: list[Text_Chunk] = [Text_Chunk(self.open_file.readline())]
            if text_chunks[0].get_text() == '':
                self.is_eof = True
        except Exception as err:
            self._readpart_except(err)
        return text_chunks