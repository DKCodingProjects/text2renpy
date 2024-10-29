from .reader import Reader
from src.misc.text_chunk_data import Text_Chunk_Data

class Raw_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)

    def open(self):
        try:
            self.open_file = open(self.file_name, 'r')
        except Exception as err:
            raise Exception('An error occured while opening file \''+self.file_name+'\' ('+f"{type(err).__name__}: {err}"+')')

    def readpart(self) -> tuple[list[Text_Chunk_Data], dict]:
        try:
            curr_text = Text_Chunk_Data(self.open_file.readline(), None)
            if curr_text.get_text() == '':
                self.is_eof = True
        except Exception as err:
            raise Exception('Something went wrong with Raw_Reader in method \'readpart\'('+f"{type(err).__name__}: {err}"+')')
        return curr_text, None