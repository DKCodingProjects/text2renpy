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
    SCENE = 7
    SHOW = 8
    SHOW_SPKR = 9
    HIDE = 10
    HIDE_SPKR = 11
    COMMENT = 12
    BLKCOMMENT = 13
    BLKCOMMENT_ROW = 14
    EMPTY = 15

    MENU = 16
    CHOICE = 17
    CODE = 18

class SRS_Blocks(Enum):
    SAY = 1
    SET = 2
    COMMENT = 3
    CHOICE = 4

class SRS_Expressions():
    special_chars = r'[^=:+>\-<]+?' # <-- TEST THIS!
    
    SET = re.compile(r'^\s*('+special_chars+r')?\s*(?:=|\:)\s*('+special_chars+r')\s*$')
    SET_LITERAL = re.compile(r'^\s*('+special_chars+r')?\s*(?:=|\:)\s*\"(.+?)\"\s*$')
    BLKSET = re.compile(r'^\s*('+special_chars+r')?\s*(?:==|\:\:)\s*('+special_chars+r')\s*$')
    BLKSET_LITERAL = re.compile(r'^\s*('+special_chars+r')?\s*(?:==|\:\:)\s*\"(.+?)\"\s*$')
    BLKSET_LITERAL_ROW = re.compile(r'^\s*\"(.+?)\"\s*$')

    SAY = re.compile(r'^.+$') # normal text
    SCENE = re.compile(r'^\s*(?:\+\+|>>)\s*('+special_chars+r')\s*$')
    SHOW = re.compile(r'^\s*(?:\+|>)\s*('+special_chars+r')\s*$')
    SHOW_SPKR = re.compile(r'^\s*(?:=\+|\:>)\s*('+special_chars+r')\s*$')
    HIDE = re.compile(r'^\s*(?:\-|<)\s*('+special_chars+r')\s*$')
    HIDE_SPKR = re.compile(r'^\s*(?:=\-|\:<)\s*('+special_chars+r')\s*$')
    COMMENT = re.compile(r'^\s*(?:\#)\s*('+special_chars+r')\s*$')
    BLKCOMMENT = re.compile(r'^\s*(?:\#\#)\s*('+special_chars+r')\s*$')
    EMPTY = re.compile(r'^\s*$')

    MENU = re.compile(r'^\s*\?\?\s*('+special_chars+r')\s*$')
    ADD_CHOICE = re.compile(r'^\s*\?(?:\+|>)\s*('+special_chars+r')\s*$')
    CODE = re.compile(r'^\s*\/\s*('+special_chars+r')\s*$')

    del special_chars

# SRS = Shorthand Ren'Py Script
class SRS_Translator(Translator):
    expr = SRS_Expressions()
    def __init__(self, script_characters: object):
        self.curr_speaker = ''
        self.script_characters = script_characters
        self.script_images = {}
    
    def _consolidate_chunks(self, text_chunks):
        return super()._consolidate_chunks(text_chunks)
    
    def convert_unicode_quotes(text):
        unicode_to_ascii = {
            '“': '"', '”': '"',  # Double quotes
            '‘': "'", '’': "'",  # Single quotes
            '«': '"', '»': '"',  # Angle quotes
            '‹': "'", '›': "'"   # Single angle quotes
        }
        pattern = re.compile('|'.join(re.escape(key) for key in unicode_to_ascii.keys()))
        converted_text = pattern.sub(lambda x: unicode_to_ascii[x.group()], text)
        return converted_text
    
    def get_type(self, chunks: list[Text_Chunk], block_type : SRS_Types) -> SRS_Types:
        trans = SRS_Translator
        expr = SRS_Expressions
        type = SRS_Types
        blck = SRS_Blocks

        chunk = self._consolidate_chunks(chunks)

        if expr.EMPTY.match(chunk):
            return type.EMPTY
        elif expr.BLKCOMMENT.match(chunk):
            return type.BLKCOMMENT
        elif block_type == blck.COMMENT:
            return type.BLKCOMMENT_ROW
        elif expr.COMMENT.match(chunk):
            return type.COMMENT
        elif expr.CODE.match(chunk):
            return type.CODE
        elif expr.BLKSET.match(chunk):
            if expr.BLKSET_LITERAL.match(trans.convert_unicode_quotes(chunk)):
                return type.BLKSET_LITERAL
            else:
                return type.BLKSET
        elif block_type == blck.SET:
            if expr.BLKSET_LITERAL_ROW.match(trans.convert_unicode_quotes(chunk)):
                return type.BLKSET_LITERAL_ROW
            else:
                return type.BLKSET_ROW
        elif expr.SET.match(chunk):
            if expr.SET_LITERAL.match(trans.convert_unicode_quotes(chunk)):
                return type.SET_LITERAL
            else:
                return type.SET
        else:
            return type.SAY