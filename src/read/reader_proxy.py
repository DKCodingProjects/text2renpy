from .reader import Reader
from .docx_reader import Docx_Reader
from .raw_reader import Raw_Reader
from .csv_reader import Csv_Reader
from pathlib import Path

class Reader_Proxy():
    def __init__(self):
        self.instanceof: Reader = Reader('')

    def _get_instance_except(self, err):
        raise Exception('An error occured in {0} while getting instance of \'{1}\' ({2})'.format(self.__class__.__name__, self.instanceof.__class__.__name__, f"{type(err).__name__}: {err}"))

    def get_instance(read_file: str):
        raw_files = {'.txt', '.rpy'}
        doc_files = {'.docx'}
        csv_files = {'.csv'}

        extension = Path(read_file).suffix
        if extension in doc_files:
            return Docx_Reader(read_file)
        elif extension in raw_files:
            return Raw_Reader(read_file)
        elif extension in csv_files:
            return Csv_Reader(read_file)
        else:
            Reader_Proxy._get_instance_except('TypeError: Extension in document \"{0}\" is not supported in Text2RenPy'.format(read_file))