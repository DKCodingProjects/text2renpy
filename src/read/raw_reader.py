from .reader import Reader

class Raw_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)

    def open(self):
        try:
            self.open_file = open(self.file_name, 'rb+')
        except Exception as err:
            raise Exception('An error occured while opening file \''+self.file_name+'\'('+f"{type(err).__name__}: {err}"+')')

    def readline(self) -> tuple[str, dict]:
        try:
            curr_text = self.open_file.readline()
            curr_attribs = None
        except Exception as err:
            raise Exception('Something went wrong with Raw_Reader('+f"{type(err).__name__}: {err}"+')')
        return curr_text, curr_attribs