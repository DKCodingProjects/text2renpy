from enum import Enum
from pathlib import Path

class Document_Type(Enum):
    RAW = 0
    MARKDOWN = 1
    FDX = 2
    DOCX = 3

class Supported_Extensions:
    raw_files = {'.txt', '.rpy'}
    md_files = {'.md', '.fountain'}
    fdx_files = {'.fdx'}
    doc_files = {'.docx'}

class Document_Metadata():
    def find_type(file_name: str) -> Document_Type:
        extension = Path(file_name).suffix
        if extension in Supported_Extensions.raw_files:
            return Document_Type.RAW
        elif extension in Supported_Extensions.md_files:
            raise TypeError('class \'Markdown_Reader\' is still being developed! Update to latest version or wait for a working release!')
            return Document_Type.MARKDOWN
        elif extension in Supported_Extensions.fdx_files:
            return Document_Type.FDX
        elif extension in Supported_Extensions.doc_files:
            return Document_Type.DOCX
        else:
            raise TypeError('document \"{0}\" is not a supported document type for Text2RenPy'.format(file_name))

    def __init__(self, doc_name: str):
        self.file_name: str = doc_name
        self.type = Document_Metadata.find_type(doc_name)
        self.font_size: float = None
        self.doc_length: int = None
    
    def set_font_size(self, size: float):
        if size is None:
            pass
        elif type(size) is float:
            self.font_size = size
        else:
            try:
                self.font_size = float(size)
            except Exception as err:
                raise TypeError(err)
    
    def get_font_size(self) -> float:
        return self.font_size
    
    def set_doc_length(self, length: int):
        if length is None:
            pass
        elif type(length) is int:
            self.doc_length = length
        else:
            try:
                self.doc_length = int(length)
            except Exception as err:
                raise TypeError(err)
    
    def get_doc_length(self) -> float:
        return self.doc_length
    
