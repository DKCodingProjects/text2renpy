from .reader import Reader
from docx import Document
from src.misc.text_chunk import Text_Chunk

class Docx_Reader(Reader):
    def __init__(self, read_file):
        super().__init__(read_file)
    
    def lowercase_dict(self, dict):
        return super().lowercase_dict(dict)

    def open(self):
        try:
            self.open_file = Document(self.file_name)
            self.content = self.open_file.paragraphs
        except Exception as err:
            raise Exception('An error ocuured while opening document \''+self.file_name+'\' ('+f"{type(err).__name__}: {err}"+')')

    def readpart(self) -> tuple[list[Text_Chunk], dict]:
        try:
            raise Exception('Docx_Reader \'readpart\' is still in development! Download latest version or wait for update.')
            for paragraph in self.content:
                for run in paragraph.runs:
                    pass
            text_chunks = ''
            curr_attrib = None
            self.is_eof = True
        except Exception as err:
            raise Exception('Something went wrong with Docx_Reader in method \'readpart\'('+f"{type(err).__name__}: {err}"+')')
        return text_chunks, curr_attrib