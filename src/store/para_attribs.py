from src.enum.para_align_enum import Paragraph_Alignment

class Paragraph_Attributes():
    def __init__(self):
        self.type: str = None
        self.alignment = Paragraph_Alignment.NONE

    def set_alignment(self, alignment: Paragraph_Alignment):
        if type(alignment) is Paragraph_Alignment:
            self.alignment = alignment
        elif type(alignment) is int:
            self.alignment = Paragraph_Alignment(alignment)
        else:
            raise TypeError('Alignment given to {0} is not of type \'{1}\' or of type \'{2}\''.format(self.__class__.__name__, Paragraph_Alignment.__name__, int.__name__))
    
    def get_alignment(self) -> Paragraph_Alignment:
        return self.alignment
    
    def set_type(self, para_type: str):
        if type(para_type) is str:
            self.type = para_type
        else:
            raise TypeError('Alignment given to {0} is not of type \'{1}\''.format(self.__class__.__name__, str.__name__))
    
    def get_type(self) -> str:
        return self.type