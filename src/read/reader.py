from abc import ABC, abstractmethod
from src.general.text_chunk import Text_Chunk

class Reader(ABC):

    def __init__(self, read_file: str):
        self.file_name: str = read_file
        self.open_file: any = None
        self.is_eof: bool = False
        # self.analyzer = None
    
    def _open_except(self, err: Exception):
        raise Exception('An error occured in {0} while opening file \'{1}\' ({2})'.format(self.__class__.__name__, self.file_name, f"{type(err).__name__}: {err}"))

    @abstractmethod
    def open(self):
        pass

    def _readpart_except(self, err: Exception):
        raise Exception('Something went wrong with {0} in method \'readpart\' ({1})'.format(self.__class__.__name__, f"{type(err).__name__}: {err}"))

    @abstractmethod
    def readpart(self) -> tuple[list[Text_Chunk], dict]:
        pass