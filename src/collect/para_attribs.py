from enum import Enum

class Paragraph_Alignment(Enum):
    UNKNOWN = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3
    JUSTIFY = 4
    OTHER = 5

class Paragraph_Attributes():
    def __init__(self):
        self.alignment = Paragraph_Alignment.UNKNOWN
        pass

    def get_attribs(paragraph):
        pass