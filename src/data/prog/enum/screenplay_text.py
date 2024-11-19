from enum import Enum

class SCREENPLAY_TEXT(Enum):
    EMPTY = -1
    NONE = 0
    TRNSTN = 1
    HEADER = 2
    ACTION = 3
    SLUGLN = 4
    CHRCTR = 5
    PRNTHT = 6
    DIALOG = 7
    METALN = 8 # for undetermined "metalines" such as Scene Headers, Slug Lines, Characters, etc
    TEXTLN = 9 # for undetermined normal text with ending punctuation