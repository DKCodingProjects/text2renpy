from .translator  import Translator
from src.store.text_chunk import *
from src.store.para_attribs import *
from src.store.doc_metadata import *
from src.format.screenplay_format import *

class Screenplay_to_Renpy(Translator):
    def __init__(self):
        super().__init__()

    def translate_except(self, err):
        return super().translate_except(err)
    
    def consolidate_chunks(self, text_chunks):
        return super().consolidate_chunks(text_chunks)
    
    def translate(self, text_chunks: list[Text_Chunk], para_attribs: Paragraph_Attributes):
        pass