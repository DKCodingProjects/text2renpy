import re
from .translator import Translator
from src.general.text_chunk import Text_Chunk
from enum import Enum

class SRS_Types(Enum):
    SET = 0
    SET_LITERAL = 1
    BLKSET = 2
    BLKSET_ROW = 3
    BLKSET_LITERAL = 4
    BLKSET_LITERAL_ROW = 5

    SAY = 6
    SAY_LITERAL = 7
    SCENE = 8
    SHOW = 9
    SHOW_SPKR = 10
    HIDE = 11
    HIDE_SPKR = 12
    COMMENT = 13
    BLKCOMMENT = 14
    BLKCOMMENT_ROW = 15
    EMPTY = 16

    MENU = 17
    MENU_CHOICE = 18
    MENU_END = 19
    CODE = 20

class SRS_Blocks(Enum):
    NONE = 1
    SET = 2
    COMMENT = 3
    MENU = 4
    CHOICE = 5

class SRS_Expressions():
    special_chars = r'[^=:+>\-<]+?' # <-- TEST THIS!
    
    SET = re.compile(r'^\s*('+special_chars+r')?\s*(?:=|\:)\s*('+special_chars+r')\s*$')
    SET_LITERAL = re.compile(r'^\s*('+special_chars+r')?\s*(?:=|\:)\s*\"(.+?)\"\s*$')
    BLKSET = re.compile(r'^\s*('+special_chars+r')?\s*(?:==|\:\:)\s*('+special_chars+r')\s*$')
    BLKSET_LITERAL = re.compile(r'^\s*('+special_chars+r')?\s*(?:==|\:\:)\s*\"(.+?)\"\s*$')
    BLKSET_LITERAL_ROW = re.compile(r'^\s*\"(.+?)\"\s*$')

    SAY = re.compile(r'^\s*(.+)$')
    SAY_LITERAL = re.compile(r'^\s*\"(.+)\"\s*$')
    SCENE = re.compile(r'^\s*(?:\+\+|>>)\s*('+special_chars+r')\s*$')
    SHOW = re.compile(r'^\s*(?:\+|>)\s*('+special_chars+r')\s*$')
    SHOW_SPKR = re.compile(r'^\s*(?:=\+|\:>)\s*('+special_chars+r')\s*$')
    HIDE = re.compile(r'^\s*(?:\-|<)\s*('+special_chars+r')\s*$')
    HIDE_SPKR = re.compile(r'^\s*(?:=\-|\:<)\s*('+special_chars+r')\s*$')
    COMMENT = re.compile(r'^\s*(?:\#)\s*('+special_chars+r')\s*$')
    BLKCOMMENT = re.compile(r'^\s*(?:\#\#)\s*('+special_chars+r')\s*$')
    EMPTY = re.compile(r'^\s*$')

    MENU = re.compile(r'^\s*\?\?\s*('+special_chars+r')\s*$')
    MENU_CHOICE = re.compile(r'^\s*\?(?:\+|>)\s*('+special_chars+r')\s*$')
    MENU_END = re.compile(r'^\s*\?(?:\-|<)\s*('+special_chars+r')\s*$')
    CODE = re.compile(r'^\s*\/\s*('+special_chars+r')\s*$')

    del special_chars

# SRS = Shorthand Ren'Py Script
class SRS_Translator(Translator):
    expr = SRS_Expressions()
    def __init__(self, script_characters: object):
        self.curr_speaker = ''
        self.vars_dict = {
            "speaker" : '',
            "label" : '',
            "_block_type" : SRS_Blocks.NONE
        }
        self.script_characters = script_characters
        self.script_images = {}
    
    def _consolidate_chunks(self, text_chunks):
        return super()._consolidate_chunks(text_chunks)
    
    
    def convert_double_quotes(text):
        unicode_to_ascii = {
            '“': '"', '”': '"',
            '«': '"', '»': '"',
            '❝': '"', '❞': '"',
            '‟': '"', '„': '"'
        }
        pattern = re.compile('|'.join(re.escape(key) for key in unicode_to_ascii.keys()))
        converted_text = pattern.sub(lambda x: unicode_to_ascii[x.group()], text)
        return converted_text
    
    def interpret_text(self, chunks: list[Text_Chunk], block_type : SRS_Types) -> tuple[list[Text_Chunk], SRS_Types]:
        trans = SRS_Translator
        expr = SRS_Expressions
        type = SRS_Types
        blck = SRS_Blocks

        chunk = self._consolidate_chunks(chunks)

        if expr.EMPTY.match(chunk):
            return None, type.EMPTY
        elif match := expr.BLKCOMMENT.match(chunk):
            return match, type.BLKCOMMENT
        elif block_type == blck.COMMENT:
            return match, type.BLKCOMMENT_ROW
        elif match := expr.COMMENT.match(chunk):
            return match, type.COMMENT
        elif match := expr.BLKSET.match(chunk):
            if match := expr.BLKSET_LITERAL.match(trans.convert_double_quotes(chunk)):
                return match, type.BLKSET_LITERAL
            else:
                return match, type.BLKSET
        elif block_type == blck.SET:
            if match := expr.BLKSET_LITERAL_ROW.match(trans.convert_double_quotes(chunk)):
                return match, type.BLKSET_LITERAL_ROW
            else:
                return match, type.BLKSET_ROW
        elif match := expr.SET.match(chunk):
            if match := expr.SET_LITERAL.match(trans.convert_double_quotes(chunk)):
                return match, type.SET_LITERAL
            else:
                return match, type.SET
        elif match := expr.CODE.match(chunk):
            return match, type.CODE
        elif match := expr.SCENE.match(chunk):
            return match, type.SCENE
        elif match := expr.SHOW_SPKR(chunk):
            return match, type.SHOW_SPKR
        elif match := expr.SHOW.match(chunk):
            return match, type.SHOW
        elif match := expr.HIDE_SPKR.match(chunk):
            return match, type.HIDE_SPKR
        elif match := expr.HIDE.match:
            return match, type.HIDE
        elif expr.MENU.match(chunk):
            return None, type.MENU
        elif match := expr.MENU_CHOICE.match(chunk):
            return None, type.MENU_CHOICE
        elif match := expr.MENU_END.match(chunk):
            return match, type.MENU_END
        else:
            if expr.SAY_LITERAL.match(trans.convert_double_quotes(chunk)):
                return None, type.SAY_LITERAL
            else:
                return None, type.SAY

    def escape_chars(self, chunk: Text_Chunk) -> str:
        chunk.text = re.sub(r'(?<!\\)\\(?!\\)', r'\\\\', chunk.text) # escape slash
        chunk.text = re.sub(r'(?<!\\)[\"]', '\\"', chunk.text)       # escape double quote
        chunk.text = re.sub(r'(?<!\\)[\']', "\\'", chunk.text)       # escape single quote
        chunk.text = re.sub(r'(?<!{){(?!{)', r'{{', chunk.text)      # escape opening curly brace
        chunk.text = re.sub(r'(?<!\[)\[(?!\[)', r'[[', chunk.text)   # escape opening square braket
        chunk.text = re.sub(r'(?<!%|\\)%(?!%)', r'\\%', chunk.text)  # escape percent sign
        chunk.text = re.sub(r'(?<!【)【(?!【)', '【【', chunk.text)   # escape opening Lenticular braket
        return chunk.text
    
    def append_tag(tag : str, chunk : Text_Chunk): return chunk.text+'{'+tag+'}'
    
    def prepend_tag(tag : str, chunk : Text_Chunk): return '{'+tag+'}'+chunk.text

    def remove_srs_prefix(prefix : str, chunks : list [Text_Chunk]) -> list[Text_Chunk]:
        chunks_index = 0
        for char in prefix:
            curr_chunk = chunks[chunks_index]
            while True:
                if found := curr_chunk.text.find(char):
                    if found + 1 < len(curr_chunk.text):
                        curr_chunk.text = curr_chunk.text[found+1:-1]
                    else:
                        curr_chunk.text = ''
                    chunks[chunks_index] = curr_chunk
                    break
                elif chunks_index >= len(chunks):
                        break
                else:
                    chunks_index += 1
        return chunks

    def translate(self, chunks : list[Text_Chunk]) -> str:
        line_str = ''
        expr_match, line_type = self.interpret_text(chunks, self.vars_dict['_block_type'])
        if expr_match is None: # chunks require in-depth handeling
            if line_type == SRS_Types.EMPTY:
                return line_str
        else:
            pass
        return line_str, line_type