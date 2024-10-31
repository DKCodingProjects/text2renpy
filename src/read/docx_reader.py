from .reader import Reader
from docx import Document
from src.collect.text_chunk import Text_Chunk

class Docx_Reader(Reader):
    def __init__(self, read_file):
        super().__init__(read_file)
    
    def open_except(self, err):
        return super().open_except(err)
        
    def open(self):
        try:
            self.open_file = Document(self.file_name)
            self.content = self.open_file.paragraphs
            self.curr_index = 0
            self.max_index = len(self.content)
        except Exception as err:
            self.open_except(err)
    
    def build_chunk(chunk) -> Text_Chunk:
        chunk_data = Text_Chunk(chunk.text)
        chunk_data.set_bold(True if (chunk.bold) else False)
        chunk_data.set_italic(True if (chunk.italic) else False)
        chunk_data.set_underline(True if (chunk.underline) else False)
        chunk_data.set_strike(True if (chunk.font.strike) else False)
        chunk_data.set_color(str(chunk.font.color.rgb) if (chunk.font.color and chunk.font.color.rgb) else None)
        chunk_data.set_size(chunk.font.size.pt if (chunk.font.size) else None)
        return chunk_data

    def find_chunks(paragraph) -> list [Text_Chunk]:
        text_chunks = []
        for run in paragraph.runs:
            text_chunks.append(Docx_Reader.build_chunk(run))
        return text_chunks

    def readpart_except(self, err):
        return super().readpart_except(err)
    
    def readpart(self) -> tuple[list[Text_Chunk], dict]:
        try:
            text_chunks = ''
            curr_attrib = {}
            if self.curr_index < self.max_index:
                curr_paragraph = self.content[self.curr_index]
                curr_attrib['alignment'] = curr_paragraph.alignment if curr_paragraph.alignment else None
                text_chunks = Docx_Reader.find_chunks(curr_paragraph)
                self.curr_index += 1
            else:
                self.is_eof = True
        except Exception as err:
            self.readpart_except(err)
        return text_chunks, curr_attrib