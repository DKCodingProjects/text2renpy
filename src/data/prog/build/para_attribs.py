from src.data.prog.enum.para_alignment import PARAGRAPH_ALIGNMENT

class Paragraph_Attributes():
    def __init__(self):
        self.type: any = None
        self.alignment = PARAGRAPH_ALIGNMENT.NONE
        self.left_indent = None
        self.right_indent = None

    def print(self):
        print('{0} Object Instance:\n  type = {1}\n  alignment = {2}\n  left_indent = {3}\n  rigth_indent = {4}'.format(self.__class__.__name__, self.type, self.alignment, self.left_indent, self.right_indent))

    def set_alignment(self, alignment: PARAGRAPH_ALIGNMENT):
        if type(alignment) is PARAGRAPH_ALIGNMENT:
            self.alignment = alignment
        else:
            raise TypeError('Alignment given to {0} is not of type \'{1}\''.format(self.__class__.__name__, PARAGRAPH_ALIGNMENT.__name__))
    
    def get_alignment(self) -> PARAGRAPH_ALIGNMENT:
        return self.alignment
    
    def set_type(self, para_type: any):
        try:
            self.type = para_type
        except Exception as err:
            raise TypeError('An error occured while setting \'type\' in {0} ({1})'.format(self.__class__.__name__, err))
    
    def get_type(self) -> any:
        return self.type

    def set_left_indent(self, indent: float):
        if indent is None:
            pass
        elif type(indent) is float:
            self.left_indent = indent
        else:
            raise TypeError('An error occured while setting \'left_indent\' in {0} ({1})'.format(self.__class__.__name__, 'argument is not of type \'float\''))
        
    def get_left_indent(self):
        return self.left_indent
    
    def set_right_indent(self, indent: float):
        if indent is None:
            pass
        elif type(indent) is float:
            self.right_indent = indent
        else:
            raise TypeError('An error occured while setting \'right_indent\' in {0} ({1})'.format(self.__class__.__name__, 'argument is not of type \'float\''))
        
    def get_right_indent(self):
        return self.right_indent