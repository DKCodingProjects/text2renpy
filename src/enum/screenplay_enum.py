from enum import Enum

class Screenplay_Enum(Enum):
    NONE = 0
    TRNSTN = 1
    HEADER = 2
    ACTION = 3
    SLUGLN = 4
    CHRCTR = 5
    PRNTHT = 6
    DIALOG = 7
    NORMAL = 8 # for undetermined normalcase
    UPPER = 9 # for undetermined uppercase
    # COMMAND = 10
    # COMMENT = 11