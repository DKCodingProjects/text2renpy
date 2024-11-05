import re
from src.enum.screenplay_enum import Screenplay_Enum
from src.enum.para_align_enum import Paragraph_Alignment
from src.store.para_attribs import *

class Screenplay_Input:
    def __init__(self):
        self.empty = re.compile(r'^\s*$')
        self.normal = re.compile(r'^\s*(.+[\.…!?~\-\"\'\)\]\}])\s*$') # Used for both Dialogue and Action (aka Narration)
        self.upper = re.compile(r'^\s*([^a-z]+?[^\.…!?~\-\"\'\]\}])\s*$') # Used for Scene Headers, Character Names, Transitions, and Commands

        char_set = r'[A-Z0-9\s_-]+?' #r'[^a-z`~!@#$%^&*\[{\]};:\'\",<\.>/?\(\)\-=+\\|]+?'
        self.transition = re.compile(r'^\s*('+char_set+r')\s+[A-Z]+:\s*$')
        self.header = re.compile(r'^\s*((?:(?:I|E|INT|EXT)\.)\s+(?:'+char_set+r'))\s*$')
        self.character = re.compile(r'^\s*((?:'+char_set+r'\.)?\s*'+char_set+r')(?:\s+\(\s*(.+?)\s*\))?\s*$')
        self.parenthetical = re.compile(r'^\s*\(([\w\s]+)\)\s*$')
    
    def match(self, text: str, para_attribs: Paragraph_Attributes) -> Screenplay_Enum:
        if type(para_attribs) is not Paragraph_Attributes:
            raise TypeError('Argument \'para_attribs\' sent to method \'match\' in class {0} is not of type Paragraph_Attributes'.format(self.__class__.__name__))
        if self.empty.match(text):
            return Screenplay_Enum.NONE
        elif self.upper.match(text):
            if self.header.match(text):
                return Screenplay_Enum.HEADER
            elif para_attribs.get_alignment() == Paragraph_Alignment.LEFT:
                return Screenplay_Enum.SLUGLN
            elif self.character.match(text) or para_attribs.get_alignment() == Paragraph_Alignment.CENTER:
                return Screenplay_Enum.CHRCTR
            elif self.transition.match(text) or para_attribs.get_alignment() == Paragraph_Alignment.RIGHT: 
                return Screenplay_Enum.TRNSTN
            else:
                return Screenplay_Enum.UPPER
        elif match := self.normal.match(text):
            if self.parenthetical.match(text):
                match = self.parenthetical.match(text)
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