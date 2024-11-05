import re
from src.enum.renpy_enum import RenPy_Enum
from src.store.para_attribs import *

class RenPy_Output:
    def __init__(self):
        pass # regex for renpy stuff here!

    def apply_tag(self, text, tag):
        start_tag = r'{'+tag+r'}'
        end_tag = r'{/'+tag+r'}'
        return start_tag + text + end_tag
    
    def abbrev_name(self, character: str) -> str:
        return
    
    def format_say(self, dialogue: str, character = ''):
        pass

