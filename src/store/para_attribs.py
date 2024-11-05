from src.enum.para_align_enum import Paragraph_Alignment

class Paragraph_Attributes():
    def __init__(self):
        self.type: any = None
        self.alignment = Paragraph_Alignment.NONE
        self.left_indent = 0.0
        self.right_indent = 0.0

    def set_alignment(self, alignment: Paragraph_Alignment):
        if type(alignment) is Paragraph_Alignment:
            self.alignment = alignment
        elif type(alignment) is int:
            self.alignment = Paragraph_Alignment(alignment)
        else:
            raise TypeError('Alignment given to {0} is not of type \'{1}\' or of type \'{2}\''.format(self.__class__.__name__, Paragraph_Alignment.__name__, int.__name__))
    
    def get_alignment(self) -> Paragraph_Alignment:
        return self.alignment
    
    def set_type(self, para_type: any):
        try:
            self.type = para_type
        except Exception as err:
            raise TypeError('An error occured when setting \'type\' in {0} ({1})'.format(self.__class__.__name__, err))
    
    def get_type(self) -> str:
        return self.type