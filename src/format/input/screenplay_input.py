from src.data.prog.default.default_screenplay import Default_Screenplay
from src.data.prog.build.doc_metadata import Document_Metadata
from src.format.regex.screenplay_regex import Screenplay_Regex
from src.data.prog.enum.screenplay_text import SCREENPLAY_TEXT
from src.data.prog.enum.para_alignment import PARAGRAPH_ALIGNMENT
from src.data.prog.build.para_attribs import *

class Screenplay_Input:
    def __init__(self, metadata: Document_Metadata):
        self.metadata: Document_Metadata = metadata
        self.regex: Screenplay_Regex = Screenplay_Regex()

    def _metaline_match(self, text: str, para_attribs: Paragraph_Attributes) -> SCREENPLAY_TEXT:
        if para_attribs.get_left_indent() is not None:
            if para_attribs.get_left_indent() > self.metadata.get_left_indent():
                new_indent = para_attribs.get_left_indent()
                if new_indent < Default_Screenplay.trnstn_indent:
                    return SCREENPLAY_TEXT.CHRCTR
                else:
                    return SCREENPLAY_TEXT.TRNSTN
        if para_attribs.get_alignment() != PARAGRAPH_ALIGNMENT.NONE:
            if para_attribs.get_alignment() != self.metadata.get_alignment():
                new_align = para_attribs.get_alignment()
                if new_align == PARAGRAPH_ALIGNMENT.CENTER:
                    return SCREENPLAY_TEXT.CHRCTR
                elif new_align == PARAGRAPH_ALIGNMENT.RIGHT:
                    return SCREENPLAY_TEXT.TRNSTN
        if self.regex.header.match(text):
            return SCREENPLAY_TEXT.HEADER
        elif self.regex.transition.match(text):
            return SCREENPLAY_TEXT.TRNSTN
        elif self.regex.character.match(text):
            return SCREENPLAY_TEXT.CHRCTR
        else:
            return SCREENPLAY_TEXT.METALN
    
    def _handle_parenthetical(self, text: str) -> SCREENPLAY_TEXT:
        if self.regex.parenthetical.match(text):
            match = self.regex.parenthetical.match(text)
            if match.group(1).strip().lower() == 'more':
                return SCREENPLAY_TEXT.NONE
            else:
                return SCREENPLAY_TEXT.PRNTHT
        return None
    
    def _textline_match(self, text: str, para_attribs: Paragraph_Attributes) -> SCREENPLAY_TEXT:
        if para_attribs.get_left_indent() is not None:
            if para_attribs.get_left_indent() > self.metadata.get_left_indent():
                if rtrn := self._handle_parenthetical(text):
                    return rtrn
                else:
                    return SCREENPLAY_TEXT.DIALOG
            else:
                return SCREENPLAY_TEXT.ACTION
        if para_attribs.get_alignment() != PARAGRAPH_ALIGNMENT.NONE:
            if para_attribs.get_alignment() != self.metadata.get_alignment():
                if rtrn := self._handle_parenthetical(text):
                    return rtrn
                else:
                    return SCREENPLAY_TEXT.TEXTLN
            else:
                return SCREENPLAY_TEXT.ACTION
        if rtrn := self._handle_parenthetical(text):
            return rtrn
        else:
            return SCREENPLAY_TEXT.TEXTLN
    
    def match(self, text: str, para_attribs: Paragraph_Attributes) -> SCREENPLAY_TEXT:
        if not isinstance(para_attribs, Paragraph_Attributes):
            raise TypeError('Argument \'para_attribs\' sent to method \'match\' in class {0} is not of type Paragraph_Attributes'.format(self.regex.__class__.__name__))
        elif isinstance(para_attribs.get_type(), SCREENPLAY_TEXT):
            return para_attribs.get_type()
        elif self.regex.empty.match(text):
            return SCREENPLAY_TEXT.EMPTY
        elif self.regex.metaline.match(text):
            return self._metaline_match(text, para_attribs)
        elif self.regex.textline.match(text):
            return self._textline_match(text, para_attribs)
        else:
            return SCREENPLAY_TEXT.NONE