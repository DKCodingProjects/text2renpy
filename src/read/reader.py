from abc import ABC, abstractmethod
from src.collect.text_chunk import Text_Chunk

class Reader(ABC):
    def __init__(self, read_file: str):
        self.file_name: str = read_file
        self.open_file = None
        self.is_eof: bool = False

    def lowercase_dict(self, dict: dict):
        return {k.lower(): v.lower() for k, v in dict.items()}
    
    @abstractmethod
    def build_chunk(chunk) -> Text_Chunk:
        return None
    
    @abstractmethod
    def find_chunks(paragraph) -> list[Text_Chunk]:
        return None

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def readpart(self) -> tuple[list[Text_Chunk], dict]:
        pass