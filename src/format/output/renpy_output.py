import re
from src.data.prog.build.text_chunk import Text_Chunk
from src.data.prog.enum.renpy_statement import RENPY_STATEMENT
from src.data.prog.build.para_attribs import *

class RenPy_Output:
    def __init__(self):
        pass # regex for renpy stuff here!

    def _apply_tag(self, text, tag):
        start_tag = r'{'+tag+r'}'
        end_tag = r'{/'+tag+r'}'
        return start_tag + text + end_tag
    
    def _remove_duplicate_tags(text: str, tag: str):
        dup_tag = re.compile(r'\{\/'+tag+r'\}(\s*)\{'+tag+r'\}')
        while match := dup_tag.search(text):
           text = re.subn(dup_tag.pattern, match.group(1), text, 1)[0]
        return text
    
    def _maintain_spacing(text: str):
        mult_spc = re.compile(r'\s(\s+)')
        while match := mult_spc.search(text):
            text = re.subn(mult_spc.pattern, r' {space='+str(len(match.group(1))*5)+r'}', text, 1)[0]
        return text
    
    def abbrev_name(self, character: str) -> str:
        pass
    
    def format_say(self, dialogue: list[Text_Chunk], character: str = '') -> tuple[str, str]: # statement, abbrev character name
        pass

    def format_show(self, name: str, value: str, prefix: str = 'show')  -> tuple[str, str]: # stament, image name
        pass

    def format_scene(self, name: str, value: str) -> tuple[str, str]: # statement, image name:
        return self.format_show(name, value, 'scene')
    
    def format_define(self, name: str, value: str, type: str = 'define',):
        return type+' '+name+' = '+value



