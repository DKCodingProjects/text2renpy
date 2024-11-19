from enum import Enum

class SCREENPLAY_TEXT(Enum):
    EMPTY = -1
    NONE = 0
    TRNSTN = 1
    HEADER = 2
    ACTION = 3
    CHRCTR = 4
    PRNTHT = 5
    DIALOG = 6
    METALN = 7 # for undetermined "metalines" such as Scene Headers, Slug Lines, Characters, etc
    TEXTLN = 8 # for undetermined normal text with ending punctuation