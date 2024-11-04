from abc import ABC, abstractmethod
from src.store.doc_metadata import *

class Document_Analysis(ABC):
    def __init__(self, read_file: str):
        self.file_name: str = read_file
    
    @abstractmethod
    def analyze_except(self, err: Exception):
        raise Exception('An error occured in {0} while analyzing file \'{1}\' ({2})'.format(self.__class__.__name__, self.file_name, f"{type(err).__name__}: {err}"))

    @abstractmethod
    def analyze(self) -> Document_Metadata:
        pass