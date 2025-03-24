import csv
from read.reader import Reader

class Cav_Reader(Reader):
    def __init__(self, read_file: str):
        self.file_name: str = read_file
        self.open_file: any = None
        self.is_eof: bool = False
        # self.analyzer = None
    
    def _open_except(self, err: Exception):
        return super()._open_except(err)

    def open(self):
        pass

    def _readpart_except(self, err):
        return super()._readpart_except(err)

    def readpart(self) -> list[str]:
        pass
    
    def readrow(self):
        return self.readpart()