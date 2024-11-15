from src.format.output.renpy_output import RenPy_Output
from .translator  import Translator
from src.data.prog.build.text_chunk import *
from src.data.prog.build.para_attribs import *
from src.data.prog.build.doc_metadata import *
from src.data.prog.enum.screenplay_text import SCREENPLAY_TEXT
from src.data.prog.enum.renpy_statement import RENPY_STATEMENT
from src.format.input.screenplay_input import *

class Screenplay_to_Renpy(Translator):
    def _placeholder_metadata() -> Document_Metadata:
        doc_meta = Document_Metadata('file.txt')
        doc_meta.set_left_indent(1.0)
        doc_meta.set_font_size(12.0)
        doc_meta.set_alignment(PARAGRAPH_ALIGNMENT.LEFT)
        doc_meta.print()
        return doc_meta
    
    def __init__(self):
        self.input_format: Screenplay_Input = Screenplay_Input(Screenplay_to_Renpy._placeholder_metadata())
        self.output_format: RenPy_Output = RenPy_Output()

    def _translate_except(err):
        return super()._translate_except(err)
    
    def _consolidate_chunks(self, text_chunks: Text_Chunk):
        return super()._consolidate_chunks(text_chunks)
    
    def translate(self, text_chunks: list[Text_Chunk], para_attribs: Paragraph_Attributes):
        consolid_text = self._consolidate_chunks(text_chunks)
        script_type = self.input_format.match(consolid_text, para_attribs)
        print('Text \"{0}\" is of type {1}'.format(consolid_text.strip(), script_type))
        # para_attribs.print()
