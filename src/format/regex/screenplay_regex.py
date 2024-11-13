import re

class Screenplay_Regex:
    def __init__(self):
        self.empty: re.Pattern = re.compile(r'^\s*$')
        self.normal: re.Pattern = re.compile(r'^\s*(.+[\.…!?~\-\"\'\)\]\}])\s*$') # Used for both Dialogue and Action (aka Narration)
        self.upper: re.Pattern = re.compile(r'^\s*([^a-z]+?[^\.…!?~\-\"\'\]\}])\s*$') # Used for Scene Headers, Character Names, Transitions, and Slug-lines

        _char_set = r'[A-Z0-9\s\-_]+?'
        self.transition: re.Pattern = re.compile(r'^\s*('+_char_set+r')\s+[A-Z]+:\s*$')
        self.header: re.Pattern = re.compile(r'^\s*([INTEXT\.\\\/]{1,9}\s+'+_char_set+r')\s*$')
        self.character: re.Pattern = re.compile(r'^\s*((?:'+_char_set+r'\.\s*)?'+_char_set+r')(?:\s+\(\s*(.+?)\s*\))?\s*$')
        self.parenthetical: re.Pattern = re.compile(r'^\s*\(([\w\s]+)\)\s*$')