from .proxy import Proxy
from src.read.raw_reader import Raw_Reader
from src.read.fdx_reader import Fdx_Reader
from src.read.docx_reader import Docx_Reader
from src.read.reader import Reader
from pathlib import Path

class Reader_Proxy(Proxy):
    raw_files = {'.txt', '.rpy'}
    fdx_files = {'.fdx'}
    doc_files = {'.docx'}
    # md_files = {'.md', '.fountain'}

    def get_instance_except(self, err):
        instance = Reader('')
        return super().get_instance_except(instance, err)

    def get_instance(read_file: str):
        extension = Path(read_file).suffix
        if extension in Reader_Proxy.doc_files:
            return Docx_Reader(read_file)
        elif extension in Reader_Proxy.fdx_files:
            return Fdx_Reader(read_file)
        elif extension in Reader_Proxy.raw_files:
            return Raw_Reader(read_file)
        else:
            Reader_Proxy.get_instance_except('TypeError: Extension in document \"{0}\" is not supported in Text2RenPy'.format(read_file))