from abc import ABC, abstractmethod
from src.data.prog.build.text_chunk import *
from src.data.prog.build.doc_metadata import *

class Translator(ABC):
    def __init__(self, doc_metadata: Document_Metadata, ):
        # add variables
        pass
    
    def _translate_except(self, err: Exception):
        raise Exception('An error occured in {0} while translating content ({1})'.format(self.__class__.__name__, f"{type(err).__name__}: {err}"))
    
    def _consolidate_chunks(self, text_chunks: list[Text_Chunk]) -> str:
        consolid_text: str = ''
        for chunk in text_chunks:
            consolid_text = consolid_text + chunk.get_text()
        return consolid_text
    
    @abstractmethod
    def translate(self, text_chunks: list[Text_Chunk]) -> str:
        pass