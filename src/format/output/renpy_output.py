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
    
    def _apply_value_tag(self, text: str, tag: str, value: any, operator: str = '='):
        start_tag = r'{'+tag+operator+str(value)+r'}'
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
    
    def _append_space(text: str) -> str:
        if text: return text+' '
        else: return text
    
    def _replace_underscore(text: str) -> str:
        return text.replace('_', ' ')
    
    def _replace_space(text: str) -> str:
        return text.replace(' ', '_')
    
    def _add_at(name: str, prefix: str = 'at') -> str:
        return prefix+' '+RenPy_Output._replace_space(name)
    
    def _add_with(name: str) -> str:
        return RenPy_Output._add_at(name, 'with')
    
    def abbrev_name(self, character: str) -> str:
        pass
    
    def format_say(self, dialogue: list[Text_Chunk], character: str = '') -> tuple[str, str]: # statement, abbrev character name
        pass

    def format_show(self, name: str, loc: str = '', trans: str = '', prefix: str = 'show')  -> tuple[str, str]: # stament, image name
        loc_str = RenPy_Output._append_space(RenPy_Output._add_at(loc) if loc else '')
        trans_str = RenPy_Output._add_with(trans) if trans else ''
        return (RenPy_Output._append_space(prefix)+RenPy_Output._append_space(RenPy_Output._replace_underscore(name))+loc_str+trans_str).strip()

    def format_scene(self, name: str, loc: str = '', trans: str = '') -> tuple[str, str]: # statement, image name:
        return self.format_show(name,  loc, trans, 'scene')
    
    def format_define(self, name: str, value: str, type: str = 'define',):
        return type+' '+name+' = '+value



