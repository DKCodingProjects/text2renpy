from .reader import Reader
import sys

class Raw_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)

    def open(self):
        try:
            self.open_file = open(self.file_name, 'r+')
        except FileNotFoundError as e:
            print(e)

    def readline(self) -> tuple[str, dict]:
        curr_line: str = ''
        try:
            curr_line = self.open_file.readline()
        except FileNotFoundError as e:
            print('read_file not opened; please open read_file first\n', e)
        return curr_line, None