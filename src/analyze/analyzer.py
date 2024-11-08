from abc import ABC, abstractmethod
from src.store.doc_metadata import *
from src.enum.para_align_enum import Paragraph_Alignment

class Document_Analyzer(ABC):
    def __init__(self, read_file: str):
        self.file_name: str = read_file
        self.dominant_size: float = None
        self.dominant_indent: float = None
        self.dominant_alignment: Paragraph_Alignment = None
    
    @abstractmethod
    def analyze_except(self, err: Exception):
        raise Exception('An error occured in {0} while analyzing file \'{1}\' ({2})'.format(self.__class__.__name__, self.file_name, f"{type(err).__name__}: {err}"))

    @abstractmethod
    def analyze(self) -> Document_Metadata:
        pass