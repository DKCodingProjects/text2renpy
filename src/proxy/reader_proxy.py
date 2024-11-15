from .proxy import Proxy
from src.read import *
from src.data.prog.support.doc_extensions import Supported_Document_Extensions
from pathlib import Path

class Reader_Proxy(Proxy):
    def _get_instance_except(self, err):
        instance = reader.Reader('')
        return super()._get_instance_except(self, instance, err)

    def get_instance(read_file: str):
        support = Supported_Document_Extensions()
        extension = Path(read_file).suffix
        if extension in support.doc_files:
            return docx_reader.Docx_Reader(read_file)
        elif extension in support.fdx_files:
            return fdx_reader.Fdx_Reader(read_file)
        elif extension in support.md_files:
            raise TypeError('class \'Markdown_Reader\' is still being developed! Update to latest version or wait for a working release!')
            return md_reader.Markdown_Reader(read_file)
        elif extension in support.raw_files:
            return raw_reader.Raw_Reader(read_file)
        else:
            Reader_Proxy._get_instance_except('TypeError: Extension in document \"{0}\" is not supported in Text2RenPy'.format(read_file))