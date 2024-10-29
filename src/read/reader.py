from abc import ABC, abstractmethod
from src.misc.text_chunk_data import Text_Chunk_Data

class Reader(ABC):
    def __init__(self, read_file: str):
        self.file_name: str = read_file
        self.open_file = None
        self.is_eof: bool = False

    def lowercase_dict(self, dict: dict):
        return {k.lower(): v.lower() for k, v in dict.items()}

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def readpart(self) -> tuple[list[Text_Chunk_Data], dict]:
        pass