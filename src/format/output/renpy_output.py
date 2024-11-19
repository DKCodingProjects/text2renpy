import re
from src.data.prog.build.text_chunk import Text_Chunk
from src.data.prog.enum.renpy_statement import RENPY_STATEMENT
from src.data.prog.build.para_attribs import *

class RenPy_Output:
    def __init__(self):
        pass # regex for renpy stuff here!

    def _apply_tag(text, tag):
        start_tag = r'{'+tag+r'}'
        end_tag = r'{/'+tag+r'}'
        return start_tag + text + end_tag
    
    def _apply_value_tag(text: str, tag: str, value: any, operator: str = '='):
        start_tag = r'{'+tag+operator+str(value)+r'}'
        end_tag = r'{/'+tag+r'}'
        return start_tag + text + end_tag
    
    def _apply_tags(chunk: Text_Chunk):
        tag_text = chunk.get_text()
        if color := chunk.get_color():
            tag_text = RenPy_Output._apply_value_tag(tag_text, 'color', '#'+color.lower())
        if chunk.get_size() != 0:
            size = chunk.get_size()
            if size > 0:
                tag_text = RenPy_Output._apply_value_tag(tag_text, 'size', size, '=+')
            else:
                tag_text = RenPy_Output._apply_value_tag(tag_text, 'size', abs(size), '=-')
        if chunk.is_bold():
            tag_text = RenPy_Output._apply_tag(tag_text, 'b')
        if chunk.is_italic():
            tag_text = RenPy_Output._apply_tag(tag_text, 'i')
        if chunk.is_underline():
            tag_text = RenPy_Output._apply_tag(tag_text, 'u')
        if chunk.is_strike():
            tag_text = RenPy_Output._apply_tag(tag_text, 's')
        return tag_text
    
    def _remove_duplicate_tag(text: str, tag: str):
        '''
        # can't get this to work!
        dup_tag = re.compile(r'(\{\/'+tag+r'\}(.*?)\{'+tag+r'\})')
        untag_text = re.compile(r'((?<=\})[^\{\}]*?(?=\{))')
        untag_space = re.compile(r'((?<=\})\s*?(?=\{))')
        finds = dup_tag.findall(text)
        for find in finds:
            if untag_text.match(find[1]) and not untag_space.match(find[1]):
                text.replace(find[0], find[1])
        '''
        return text
    
    def _remove_duplicate_tags(text: str):
        tags = ['s', 'u', 'i', 'b'] # value based tags are ignored
        for tag in tags:
            text = RenPy_Output._remove_duplicate_tag(text, tag)
        return text
    
    def _maintain_spacing(text: str):
        mult_spc = re.compile(r'\s(\s+)')
        while match := mult_spc.search(text):
            text = re.subn(mult_spc.pattern, r' {space='+str(len(match.group(1))*5)+r'}', text, 1)[0]
        return text
    
    def _replace_underscore(text: str) -> str:
        return text.replace('_', ' ')
    
    def _replace_space(text: str) -> str:
        return text.replace(' ', '_')
    
    def _add_at(name: str, prefix: str = 'at') -> str:
        return prefix+' '+RenPy_Output._replace_space(name)
    
    def _add_with(name: str) -> str:
        return RenPy_Output._add_at(name, 'with')
    
    def abbrev_name(name: str) -> str:
        return name[0:1].lower() if len(name) >= 2 else (name[0]+name[0]).lower()
    
    def format_say(text_chunks: list[Text_Chunk], character: str = ''): # statement, abbrev character name
        character = character+' ' if character else ''
        rtrn_text = ''
        for chunk in text_chunks:
            curr_text = chunk.get_text()
            if chunk.has_style:
                curr_text = RenPy_Output._apply_tags(chunk)
            rtrn_text = rtrn_text+curr_text
        # rtrn_text = RenPy_Output._remove_duplicate_tags(rtrn_text)
        rtrn_text = RenPy_Output._maintain_spacing(rtrn_text)
        return f'{character}\"{rtrn_text}\"'

    def format_show(name: str, loc: str = '', trans: str = '', prefix: str = 'show')  -> tuple[str, str]: # stament, image name
        loc_str = ' '+RenPy_Output._add_at(loc) if loc else ''
        trans_str = ' '+RenPy_Output._add_with(trans) if trans else ''
        return prefix+' '+RenPy_Output._replace_underscore(name)+loc_str+trans_str

    def format_scene(name: str, loc: str = '', trans: str = '') -> tuple[str, str]: # statement, image name:
        return RenPy_Output.format_show(name,  loc, trans, 'scene')
    
    def format_define(name: str, value: str, type: str = 'define'):
        return type+' '+name+' = '+value
    
    def format_chrctr(self):
        pass



