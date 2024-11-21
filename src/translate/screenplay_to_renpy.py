from .translator import Translator
from src.data.prog.build.text_chunk import *
from src.data.prog.build.para_attribs import *
from src.data.prog.build.doc_metadata import *
from src.data.prog.enum.screenplay_text import SCREENPLAY_TEXT
from src.data.prog.enum.renpy_statement import RENPY_STATEMENT
from src.format.input.screenplay_input import *
from src.translate.record.scrnply_trckr import Screenplay_Tracker

class Screenplay_to_Renpy(Translator):
    def _placeholder_metadata() -> Document_Metadata:
        doc_meta = Document_Metadata('file.txt')
        doc_meta.set_left_indent(1.0)
        doc_meta.set_font_size(12.0)
        doc_meta.set_alignment(PARAGRAPH_ALIGNMENT.LEFT)
        return doc_meta
    
    def __init__(self):
        self.input_format: Screenplay_Input = Screenplay_Input(Screenplay_to_Renpy._placeholder_metadata())
        self.input_tracker = Screenplay_Tracker()
        self.output_recorder = None

    def _translate_except(err):
        return super()._translate_except(err)
    
    def _consolidate_chunks(self, text_chunks: Text_Chunk):
        return super()._consolidate_chunks(text_chunks)
    
    def translate(self, text_chunks: list[Text_Chunk], para_attribs: Paragraph_Attributes) -> tuple[SCREENPLAY_TEXT, RENPY_STATEMENT]:
        consolid_text = self._consolidate_chunks(text_chunks).strip()
        input_type = self.input_format.match(consolid_text, para_attribs)
        output_type = RENPY_STATEMENT.EMPTY
        if input_type != SCREENPLAY_TEXT.EMPTY:
            if input_type == SCREENPLAY_TEXT.ACTION:
                output_type = RENPY_STATEMENT.SAY
            elif input_type == SCREENPLAY_TEXT.DIALOG:
                output_type = RENPY_STATEMENT.SAY
            elif input_type == SCREENPLAY_TEXT.CHRCTR:
                output_type = RENPY_STATEMENT.CHROBJ
            elif input_type == SCREENPLAY_TEXT.PRNTHT:
                self.input_tracker.set_prnth(consolid_text)
                output_type = RENPY_STATEMENT.SHOW
            elif input_type == SCREENPLAY_TEXT.TRNSTN:
                self.input_tracker.set_trnstn(consolid_text)
                # output_type = RENPY_STATEMENT.EMPTY
            elif input_type == SCREENPLAY_TEXT.HEADER:
                output_type = RENPY_STATEMENT.SCENE
            elif input_type == SCREENPLAY_TEXT.METALN:
                output_type = RENPY_STATEMENT.MANY
            else: # input_type == SCREENPLAY_TEXT.TEXTLN
                output_type = RENPY_STATEMENT.SAY
        else:
            # output_type = RENPY_STATEMENT.EMPTY
            self.input_tracker.set_spkr('')
            self.input_tracker.set_prnth('')
        
        return input_type, output_type
