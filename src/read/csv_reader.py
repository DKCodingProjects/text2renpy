import csv
from .reader import Reader

class Csv_Reader(Reader):
    def __init__(self, read_file):
        super().__init__(read_file)
        self.headers : list = []
    
    def _open_except(self, err: Exception):
        return super()._open_except(err)

    def open(self, has_headers = True):
        try:
            csvfile = open(self.file_name, newline='')
            self.open_file = csv.reader(csvfile)
            if has_headers:
                self.headers = self.open_file.__next__()
        except Exception as err:
            self._open_except(err)

    def _readpart_except(self, err):
        return super()._readpart_except(err)

    def readpart(self) -> list[str]:
        row = []
        try:
            if not self.is_eof:
                row = next(self.open_file, [])
        except Exception as err:
            self._readpart_except(err)
        if not row:
            self.is_eof = True
        return row
    
    def readrow(self):
        return self.readpart()