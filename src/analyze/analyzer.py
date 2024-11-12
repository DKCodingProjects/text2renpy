from abc import ABC, abstractmethod
from src.data.prog.build.doc_metadata import *
from src.data.prog.enum.para_alignment import PARAGRAPH_ALIGNMENT

class Document_Analyzer(ABC):
    def __init__(self, read_file: str):
        self.metadata: Document_Metadata = Document_Metadata(read_file)
        # Delete the following
        self.file_name: str = read_file
        self.dominant_size: float = None
        self.dominant_indent: float = None
        self.dominant_alignment: PARAGRAPH_ALIGNMENT = None
    
    @abstractmethod
    def analyze_except(self, err: Exception):
        raise Exception('An error occured in {0} while analyzing file \'{1}\' ({2})'.format(self.__class__.__name__, self.file_name, f"{type(err).__name__}: {err}"))

    @abstractmethod
    def analyze(self):
        pass