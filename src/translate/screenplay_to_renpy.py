from .translator  import Translator
from src.store.text_chunk import *
from src.store.para_attribs import *
from src.store.doc_metadata import *
from src.format.input.screenplay_input import *

class Screenplay_to_Renpy(Translator):
    def __init__(self):
        self.input_format = Screenplay_Input()

    def _translate_except(err):
        return super()._translate_except(err)
    
    def _consolidate_chunks(self, text_chunks: Text_Chunk):
        return super()._consolidate_chunks(text_chunks)
    
    def translate(self, text_chunks: list[Text_Chunk], para_attribs: Paragraph_Attributes):
        consolid_text = self._consolidate_chunks(text_chunks)
        script_type = self.input_format.match(consolid_text, para_attribs)
        print('Text \"{0}\" is of type {1}'.format(consolid_text.strip(), script_type))
        # para_attribs.print()
