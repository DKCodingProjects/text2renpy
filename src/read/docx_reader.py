from .reader import Reader
import docx
from src.data.prog.build.text_chunk import Text_Chunk

class Docx_Reader(Reader):
    def __init__(self, read_file):
        super().__init__(read_file)
    
    def _open_except(self, err):
        return super()._open_except(err)
        
    def open(self):
        try:
            self.open_file = docx.Document(self.file_name)
            self.content = self.open_file.paragraphs
            self.curr_index = 0
            self.max_index = len(self.content)
        except Exception as err:
            self._open_except(err)
    
    def _calc_size(size):
        size_diff = size - 11 # CHANGE VALUE LATER!!!
        if size_diff >= 1.0 or size_diff <= -1.0:
            return size_diff
        else:
            return None
    
    def _build_chunk(chunk: docx.text.run.Run) -> Text_Chunk:
        chunk_data = Text_Chunk(chunk.text)
        chunk_data.set_bold(True if (chunk.bold) else False)
        chunk_data.set_italic(True if (chunk.italic) else False)
        chunk_data.set_underline(True if (chunk.underline) else False)
        chunk_data.set_strike(True if (chunk.font.strike) else False)
        chunk_data.set_color(str(chunk.font.color.rgb) if (chunk.font.color and chunk.font.color.rgb) else None)
        chunk_data.set_size(Docx_Reader._calc_size(chunk.font.size.pt) if (chunk.font.size) else None)
        return chunk_data

    def _find_chunks(paragraph: docx.text.paragraph.Paragraph) -> list[Text_Chunk]:
        text_chunks = []
        for run in paragraph.runs:
            text_chunks.append(Docx_Reader._build_chunk(run))
        return text_chunks

    def _readpart_except(self, err):
        return super()._readpart_except(err)
    
    def readpart(self) -> list[Text_Chunk]:
        try:
            text_chunks: list[Text_Chunk] = []
            if self.curr_index < self.max_index:
                curr_paragraph = self.content[self.curr_index]
                text_chunks = Docx_Reader._find_chunks(curr_paragraph)
                self.curr_index += 1
            else:
                self.is_eof = True
        except Exception as err:
            self._readpart_except(err)
        return text_chunks