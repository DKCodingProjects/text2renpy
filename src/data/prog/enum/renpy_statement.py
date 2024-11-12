from enum import Enum

class RENPY_STATEMENT(Enum):
    EMPTY = -1
    NONE = 0
    SAY = 1
    SHOW = 2
    SCENE = 3
    AUDIO = 4
    VOICE = 5
    SOUND = 6
    MUSIC = 7
    IMAGE = 8
    DEFINE = 9