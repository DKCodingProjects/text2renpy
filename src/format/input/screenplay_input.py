from src.format.regex.screenplay_regex import Screenplay_Regex
from src.enum.screenplay_enum import Screenplay_Enum
from src.enum.para_align_enum import Paragraph_Alignment
from src.store.para_attribs import *

class Screenplay_Input:
    def __init__(self):
        self.regex = Screenplay_Regex()
    
    def match(self, text: str, para_attribs: Paragraph_Attributes) -> Screenplay_Enum:
        if type(para_attribs) is not Paragraph_Attributes:
            raise TypeError('Argument \'para_attribs\' sent to method \'match\' in class {0} is not of type Paragraph_Attributes'.format(self.regex.__class__.__name__))
        if type(para_attribs.get_type()) is Screenplay_Enum:
            # if type is ACTION or HEADER check if its a slugline
            return para_attribs.get_type()
        if self.regex.empty.match(text):
            return Screenplay_Enum.EMPTY
        elif self.regex.upper.match(text):
            if self.regex.header.match(text):
                return Screenplay_Enum.HEADER
            elif para_attribs.get_alignment() == Paragraph_Alignment.LEFT:
                return Screenplay_Enum.SLUGLN
            elif self.regex.character.match(text) or para_attribs.get_alignment() == Paragraph_Alignment.CENTER:
                return Screenplay_Enum.CHRCTR
            elif self.regex.transition.match(text) or para_attribs.get_alignment() == Paragraph_Alignment.RIGHT: 
                return Screenplay_Enum.TRNSTN
            else:
                return Screenplay_Enum.UPPER
        elif match := self.regex.normal.match(text):
            if self.regex.parenthetical.match(text):
                match = self.regex.parenthetical.match(text)
                if match.group(1).lower() == 'more':
                    return Screenplay_Enum.NONE
                else:
                    return Screenplay_Enum.PRNTHT
            elif para_attribs.get_alignment() == Paragraph_Alignment.LEFT:
                return Screenplay_Enum.ACTION
            elif para_attribs.get_alignment() == Paragraph_Alignment.CENTER:
                return Screenplay_Enum.DIALOG
            else:
                return Screenplay_Enum.NORMAL
        else:
            return Screenplay_Enum.NONE