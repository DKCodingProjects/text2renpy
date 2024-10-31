import docx.document
import docx.enum
import docx.enum.text
import docx.text
import docx.text.paragraph
import docx.text.run
from .reader import Reader
import docx
from src.collect.text_chunk import Text_Chunk
from src.collect.para_attribs import *

class Docx_Reader(Reader):
    def __init__(self, read_file):
        super().__init__(read_file)
    
    def open_except(self, err):
        return super().open_except(err)
        
    def open(self):
        try:
            self.open_file = docx.Document(self.file_name)
            self.content = self.open_file.paragraphs
            self.curr_index = 0
            self.max_index = len(self.content)
        except Exception as err:
            self.open_except(err)

    def find_alignment(alignment: docx.enum.text.WD_ALIGN_PARAGRAPH) -> Paragraph_Alignment:
        if alignment is None:
            return Paragraph_Alignment(0)
        elif alignment.value == docx.enum.text.WD_ALIGN_PARAGRAPH.LEFT:
            return Paragraph_Alignment(1)
        elif alignment.value == docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER:
            return Paragraph_Alignment(2)
        elif alignment.value == docx.enum.text.WD_ALIGN_PARAGRAPH.RIGHT:
            return Paragraph_Alignment(3)
        elif alignment.value == docx.enum.text.WD_ALIGN_PARAGRAPH.JUSTIFY:
            return Paragraph_Alignment(4)
        elif alignment.value >= docx.enum.text.WD_ALIGN_PARAGRAPH.DISTRIBUTE:
            return Paragraph_Alignment(5)
        else:
            return Paragraph_Alignment(0)
    
    def build_attributes(paragraph: docx.text.paragraph.Paragraph) -> Paragraph_Attributes:
        para_attrib = Paragraph_Attributes()
        para_attrib.set_alignment(Docx_Reader.find_alignment(paragraph.alignment))
        return para_attrib
    
    def build_chunk(chunk: docx.text.run.Run) -> Text_Chunk:
        chunk_data = Text_Chunk(chunk.text)
        chunk_data.set_bold(True if (chunk.bold) else False)
        chunk_data.set_italic(True if (chunk.italic) else False)
        chunk_data.set_underline(True if (chunk.underline) else False)
        chunk_data.set_strike(True if (chunk.font.strike) else False)
        chunk_data.set_color(str(chunk.font.color.rgb) if (chunk.font.color and chunk.font.color.rgb) else None)
        chunk_data.set_size(chunk.font.size.pt if (chunk.font.size) else None)
        return chunk_data

    def find_chunks(paragraph: docx.text.paragraph.Paragraph) -> list[Text_Chunk]:
        text_chunks = []
        for run in paragraph.runs:
            text_chunks.append(Docx_Reader.build_chunk(run))
        return text_chunks

    def readpart_except(self, err):
        return super().readpart_except(err)
    
    def readpart(self) -> tuple[list[Text_Chunk], dict]:
        try:
            text_chunks: list[Text_Chunk] = []
            para_attribs: Paragraph_Attributes = None
            if self.curr_index < self.max_index:
                curr_paragraph = self.content[self.curr_index]
                para_attribs = Docx_Reader.build_attributes(curr_paragraph)
                text_chunks = Docx_Reader.find_chunks(curr_paragraph)
                self.curr_index += 1
            else:
                self.is_eof = True
        except Exception as err:
            self.readpart_except(err)
        return text_chunks, para_attribs