from abc import ABC, abstractmethod
from src.store.text_chunk import *
from src.store.para_attribs import *
from src.store.doc_metadata import *

class Translator(ABC):
    def __init__(self):
        # add variables
        pass
    
    def translate_except(self, err: Exception):
        raise Exception('An error occured in {0} while translating content ({1})'.format(self.__class__.__name__, f"{type(err).__name__}: {err}"))
    
    def consolidate_chunks(self, text_chunks: list[Text_Chunk]) -> str:
        consolid_text: str = ''
        for chunk in text_chunks:
            consolid_text = consolid_text + chunk.get_text()
        return consolid_text
    
    @abstractmethod
    def translate(self, text_chunks: list[Text_Chunk], para_attribs: Paragraph_Attributes):
        pass