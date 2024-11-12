from src.format.regex.screenplay_regex import Screenplay_Regex
from src.enum.screenplay_enum import SCREENPLAY_FORMAT
from src.enum.para_align_enum import PARAGRAPH_ALIGNMENT
from src.store.para_attribs import *

class Screenplay_Input:
    def __init__(self):
        self.regex = Screenplay_Regex()
    
    def match(self, text: str, para_attribs: Paragraph_Attributes) -> SCREENPLAY_FORMAT:
        if type(para_attribs) is not Paragraph_Attributes:
            raise TypeError('Argument \'para_attribs\' sent to method \'match\' in class {0} is not of type Paragraph_Attributes'.format(self.regex.__class__.__name__))
        if type(para_attribs.get_type()) is SCREENPLAY_FORMAT:
            # if type is ACTION or HEADER check if its a slugline
            return para_attribs.get_type()
        if self.regex.empty.match(text):
            return SCREENPLAY_FORMAT.EMPTY
        elif self.regex.upper.match(text):
            if self.regex.header.match(text):
                return SCREENPLAY_FORMAT.HEADER
            elif para_attribs.get_alignment() == PARAGRAPH_ALIGNMENT.LEFT:
                return SCREENPLAY_FORMAT.SLUGLN
            elif self.regex.character.match(text) or para_attribs.get_alignment() == PARAGRAPH_ALIGNMENT.CENTER:
                return SCREENPLAY_FORMAT.CHRCTR
            elif self.regex.transition.match(text) or para_attribs.get_alignment() == PARAGRAPH_ALIGNMENT.RIGHT: 
                return SCREENPLAY_FORMAT.TRNSTN
            else:
                return SCREENPLAY_FORMAT.UPPER
        elif match := self.regex.normal.match(text):
            if self.regex.parenthetical.match(text):
                match = self.regex.parenthetical.match(text)
                if match.group(1).lower() == 'more':
                    return SCREENPLAY_FORMAT.NONE
                else:
                    return SCREENPLAY_FORMAT.PRNTHT
            elif para_attribs.get_alignment() == PARAGRAPH_ALIGNMENT.LEFT:
                return SCREENPLAY_FORMAT.ACTION
            elif para_attribs.get_alignment() == PARAGRAPH_ALIGNMENT.CENTER:
                return SCREENPLAY_FORMAT.DIALOG
            else:
                return SCREENPLAY_FORMAT.NORMAL
        else:
            return SCREENPLAY_FORMAT.NONE