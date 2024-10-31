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
    def open_except(self, err: Exception):
        raise Exception('An error occured in {0} while opening file \'{1}\' ({2})'.format(self.__class__, self.file_name, f"{type(err).__name__}: {err}"))

    @abstractmethod
    def open(self):
        pass

    def readpart_except(self, err: Exception):
        raise Exception('Something went wrong with {0} in method \'readpart\'({1})'.format(self.__class__, f"{type(err).__name__}: {err}"))

    @abstractmethod
    def readpart(self) -> tuple[list[Text_Chunk], dict]:
        pass