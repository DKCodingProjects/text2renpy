from abc import ABC, abstractmethod

class Reader(ABC):
    def __init__(self, read_file: str):
        self.file_name: str = read_file
        self.open_file = None
        self.is_eof: bool = False

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def read(self):
        pass