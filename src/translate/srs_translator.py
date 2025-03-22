import re
from .translator import Translator
from src.general.text_chunk import Text_Chunk

# SRS = Shorthand Ren'Py Script
class SRS_Translator(Translator):
    def __init__(self, script_characters: object):
        self.curr_speaker = ''
        self.script_characters = script_characters
        self.script_images = {}
    
    def translate(self, input: list[Text_Chunk]) -> str:
        return ''