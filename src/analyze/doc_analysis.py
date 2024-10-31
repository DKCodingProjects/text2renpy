from abc import ABC, abstractmethod

class Document_Analysis(ABC):
    def __init__(self, read_file: str):
        self.file_name: str = read_file
    
    @abstractmethod
    def analyze(self):
        pass