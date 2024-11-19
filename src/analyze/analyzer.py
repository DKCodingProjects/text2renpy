from abc import ABC, abstractmethod
from src.data.prog.build.doc_metadata import *
from src.data.prog.enum.para_alignment import PARAGRAPH_ALIGNMENT

class Analyzer(ABC):
    def __init__(self, read_file: str):
        self.metadata: Document_Metadata = Document_Metadata(read_file)
        # Delete the following
        self.file_name: str = read_file
        self.dom_size: float = None
        self.dom_indent: float = None
        self.dom_alignment: PARAGRAPH_ALIGNMENT = PARAGRAPH_ALIGNMENT.NONE

    def print(self):
         print('{0} Object Instance:\n  file_name = {1}\n  dom_size = {2}\n  dom_indent = {3}\n  dom_alignment = {4}'.format(self.__class__.__name__, self.file_name, self.dom_size, self.dom_indent, self.dom_alignment))
    
    def _analyze_except(self, err: Exception):
        raise Exception('An error occured in {0} while analyzing file \'{1}\' ({2})'.format(self.__class__.__name__, self.file_name, f"{type(err).__name__}: {err}"))

    @abstractmethod
    def analyze(self):
        pass