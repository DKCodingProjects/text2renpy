from enum import Enum

class Document_Types(Enum):
    NONE = 0
    RAW = 1
    MARKDOWN = 2
    FDX = 3
    DOCX = 4

class Document_Metadata():
    def __init__(self):
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
    
