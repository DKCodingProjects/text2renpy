from src.data.prog.enum.document_type import DOCUMENT_TYPE
from src.data.prog.support.doc_extensions import Supported_Document_Extensions
from pathlib import Path

class Document_Metadata():
    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.type: DOCUMENT_TYPE = Document_Metadata._find_type(file_name)
        self.font_size: float = None
        self.left_indent: float = None

    def _find_type(file_name: str) -> DOCUMENT_TYPE:
        support = Supported_Document_Extensions()
        extension = Path(file_name).suffix
        if extension in support.doc_files:
            return DOCUMENT_TYPE.DOCX
        elif extension in support.raw_files:
            return DOCUMENT_TYPE.RAW
        else:
            raise TypeError('document \"{0}\" is not a supported document type for Text2RenPy'.format(file_name))
    
    def print(self):
        print('{0} Object Instance:\n  type = {1}\n  alignment = {2}\n  left_indent = {3}\n  font_size = {4}'.format(self.__class__.__name__, self.type, None, self.left_indent, self.font_size))

    def set_font_size(self, size: float):
        if size is None:
            pass
        elif isinstance(size, float):
            self.font_size = size
        else:
            try:
                self.font_size = float(size)
            except Exception as err:
                raise TypeError(err)
    
    def get_font_size(self) -> float:
        return self.font_size
