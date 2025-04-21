import re
from .translator import Translator
from src.general.text_chunk import Text_Chunk

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
    COMMENT = re.compile(r'^\s*(?:\#|\/)\s*('+special_chars+r')\s*$')
    BLKCOMMENT = re.compile(r'^\s*(?:\#\#|\/\/)\s*('+special_chars+r')\s*$')
    EMPTY = re.compile(r'^\s*$')

    CHOICE = re.compile(r'^\s*\?\s*('+special_chars+r')\s*$')
    BLKCHOICE = re.compile(r'^\s*\?\?\s*('+special_chars+r')\s*$')
    CODE = re.compile(r'^\s*\/\s*('+special_chars+r')\s*$')

    # ^\s*\?\s*([^=:+>\-<]+?)\s*$

    del special_chars

# SRS = Shorthand Ren'Py Script
class SRS_Translator(Translator):
    expr = SRS_Expressions()
    def __init__(self, script_characters: object):
        self.curr_speaker = ''
        self.script_characters = script_characters
        self.script_images = {}
    
    def translate(self, input: list[Text_Chunk]) -> str:
        return ''