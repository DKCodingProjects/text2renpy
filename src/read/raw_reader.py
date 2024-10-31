from .reader import Reader
from src.collect.text_chunk import Text_Chunk

class Raw_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)
    
    def open_except(self, err):
        return super().open_except(err)
    
    def open(self):
        try:
            self.open_file = open(self.file_name, 'r')
        except Exception as err:
            self.open_except(err)
        
    def readpart_except(self, err):
        return super().readpart_except(err)

    def readpart(self) -> tuple[list[Text_Chunk], dict]:
        try:
            text_chunks = Text_Chunk(self.open_file.readline())
            if text_chunks.get_text() == '':
                self.is_eof = True
        except Exception as err:
            self.readpart_except(err)
        return text_chunks, None