from .reader import Reader
import docx
from src.data.prog.build.text_chunk import Text_Chunk
from src.data.prog.build.para_attribs import *

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

    def _find_alignment(alignment: docx.enum.text.WD_ALIGN_PARAGRAPH) -> PARAGRAPH_ALIGNMENT:
        if alignment is None:
            return PARAGRAPH_ALIGNMENT.NONE
        elif alignment.value == docx.enum.text.WD_ALIGN_PARAGRAPH.LEFT:
            return PARAGRAPH_ALIGNMENT.LEFT
        elif alignment.value == docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER:
            return PARAGRAPH_ALIGNMENT.CENTER
        elif alignment.value == docx.enum.text.WD_ALIGN_PARAGRAPH.RIGHT:
            return PARAGRAPH_ALIGNMENT.RIGHT
        elif alignment.value == docx.enum.text.WD_ALIGN_PARAGRAPH.JUSTIFY:
            return PARAGRAPH_ALIGNMENT.JUSTFY
        elif alignment.value >= docx.enum.text.WD_ALIGN_PARAGRAPH.DISTRIBUTE:
            return PARAGRAPH_ALIGNMENT.OTHER
        else:
            return PARAGRAPH_ALIGNMENT.NONE
    
    def _build_attributes(paragraph: docx.text.paragraph.Paragraph) -> Paragraph_Attributes:
        para_attrib = Paragraph_Attributes()
        para_attrib.set_alignment(Docx_Reader._find_alignment(paragraph.alignment))
        para_attrib.set_left_indent(paragraph.paragraph_format.left_indent.inches if paragraph.paragraph_format.left_indent else None)
        return para_attrib
    
    def _build_chunk(chunk: docx.text.run.Run) -> Text_Chunk:
        chunk_data = Text_Chunk(chunk.text)
        chunk_data.set_bold(True if (chunk.bold) else False)
        chunk_data.set_italic(True if (chunk.italic) else False)
        chunk_data.set_underline(True if (chunk.underline) else False)
        chunk_data.set_strike(True if (chunk.font.strike) else False)
        chunk_data.set_color(str(chunk.font.color.rgb) if (chunk.font.color and chunk.font.color.rgb) else None)
        chunk_data.set_size(chunk.font.size.pt if (chunk.font.size) else None)
        return chunk_data

    def _find_chunks(paragraph: docx.text.paragraph.Paragraph) -> list[Text_Chunk]:
        text_chunks = []
        for run in paragraph.runs:
            text_chunks.append(Docx_Reader._build_chunk(run))
        return text_chunks

    def _readpart_except(self, err):
        return super()._readpart_except(err)
    
    def readpart(self) -> tuple[list[Text_Chunk], Paragraph_Attributes]:
        try:
            text_chunks: list[Text_Chunk] = []
            para_attribs: Paragraph_Attributes = Paragraph_Attributes()
            if self.curr_index < self.max_index:
                curr_paragraph = self.content[self.curr_index]
                para_attribs = Docx_Reader._build_attributes(curr_paragraph)
                text_chunks = Docx_Reader._find_chunks(curr_paragraph)
                self.curr_index += 1
            else:
                self.is_eof = True
        except Exception as err:
            self._readpart_except(err)
        return text_chunks, para_attribs