from .raw_reader import Raw_Reader
from .fdx_reader import Fdx_Reader
from .docx_reader import Docx_Reader
from pathlib import Path

class Reader_Proxy:
    raw_files = {'.txt', '.rpy'}
    fdx_files = {'.fdx'}
    doc_files = {'.docx'}
    # md_files = {'.md', '.fountain'}
    def __init__(self):
        pass

    def get_reader(read_file: str):
        extension = Path(read_file).suffix
        if extension in Reader_Proxy.doc_files:
            return Docx_Reader(read_file)
        elif extension in Reader_Proxy.fdx_files:
            return Fdx_Reader(read_file)
        elif extension in Reader_Proxy.raw_files:
            return Raw_Reader(read_file)
        else:
            raise TypeError('document \"'+read_file+'\" is not a supported document for Text2RenPy')