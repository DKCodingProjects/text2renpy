from src.enum.doc_type_enum import Document_Type
from src.enum.para_align_enum import Paragraph_Alignment
from pathlib import Path

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

    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.type: Document_Type = Document_Metadata.find_type(file_name)
        self.font_size: float = None
        self.left_indent: float = None
        self.alignment: Paragraph_Alignment = None
    
    def print(self):
        print('{0} Object Instance:\n  type = {1}\n  alignment = {2}\n  left_indent = {3}\n  font_size = {4}'.format(self.__class__.__name__, self.type, self.alignment, self.left_indent, self.font_size))

    
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
    
    def set_left_indent(self, indent: float):
        if indent is None:
            pass
        elif type(indent) is float:
            self.left_indent = indent
        else:
            try:
                self.left_indent = float(indent)
            except Exception as err:
                raise TypeError(err)
    
    def get_left_indent(self) -> float:
        return self.left_indent
    
    def set_alignment(self, alignment: float):
        if alignment is None:
            pass
        elif type(alignment) is Paragraph_Alignment:
            self.alignment = alignment
        else:
            raise TypeError('Error')
    
    def get_alignment(self) -> float:
        return self.alignment
