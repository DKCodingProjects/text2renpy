import re

class Screenplay_Regex:
    def __init__(self):
        self.empty: re.Pattern = re.compile(r'^\s*$')
        self.textline: re.Pattern = re.compile(r'^\s*(.+[\.…!?~\-\"\'\)\]\}])\s*$') # Used for both Dialogue and Action (aka Narration)
        self.metaline: re.Pattern = re.compile(r'^\s*([^a-z]+?[^\.…!?~\-\"\'\]\}])\s*$') # Used for Scene Headers, Character Names, Transitions, Slug-lines, etc.

        _char_set = r'[A-Z0-9\s\-_]+?'
        self.transition: re.Pattern = re.compile(r'^\s*('+_char_set+r')\s+[A-Z]+:\s*$')
        self.header: re.Pattern = re.compile(r'^\s*([INTEXT\.\\\/]{1,9}\s+'+_char_set+r')\s*$')
        self.character: re.Pattern = re.compile(r'^\s*((?:'+_char_set+r'\.\s*)?'+_char_set+r')(?:\s+\(\s*(.+?)\s*\))\s*$') # only works if character name has an extension
        self.parenthetical: re.Pattern = re.compile(r'^\s*\(([\w\s]+)\)\s*$')