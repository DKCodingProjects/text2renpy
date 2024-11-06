import re

class Screenplay_Regex:
    def __init__(self):
        self.empty = re.compile(r'^\s*$')
        self.normal = re.compile(r'^\s*(.+[\.…!?~\-\"\'\)\]\}])\s*$') # Used for both Dialogue and Action (aka Narration)
        self.upper = re.compile(r'^\s*([^a-z]+?[^\.…!?~\-\"\'\]\}])\s*$') # Used for Scene Headers, Character Names, Transitions, and Commands

        char_set = r'[A-Z0-9\s\-_]+?' #r'[^a-z`~!@#$%^&*\[{\]};:\'\",<\.>/?\(\)\-=+\\|]+?'
        self.transition = re.compile(r'^\s*('+char_set+r')\s+[A-Z]+:\s*$')
        self.header = re.compile(r'^\s*([INTEXT\.\\\/]{1,9}\s+'+char_set+r')\s*$')
        self.character = re.compile(r'^\s*((?:'+char_set+r'\.)?\s*'+char_set+r')(?:\s+\(\s*(.+?)\s*\))?\s*$')
        self.parenthetical = re.compile(r'^\s*\(([\w\s]+)\)\s*$')