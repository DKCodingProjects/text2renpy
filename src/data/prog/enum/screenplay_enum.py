from enum import Enum

class SCREENPLAY_FORMAT(Enum):
    EMPTY = -1
    NONE = 0
    TRNSTN = 1
    HEADER = 2
    ACTION = 3
    SLUGLN = 4
    CHRCTR = 5
    PRNTHT = 6
    DIALOG = 7
    NORMAL = 8 # for undetermined normalcase text ending with punctuation
    UPPER = 9 # for undetermined uppercase without ending punctuation