import re
from enum import Enum
from src.store.para_attribs import *

class RenPy_Enum(Enum):
    NONE = 0
    SAY = 1
    SHOW = 2
    SCENE = 3
    AUDIO = 4
    VOICE = 5
    SOUND = 6
    MUSIC = 7
    IMAGE = 8
    DEFINE = 9

class RenPy_Format:
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

