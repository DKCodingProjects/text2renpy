from enum import Enum

class RENPY_STATEMENT(Enum):
    MANY = -2 # Indicates that the input could lead to numerous Ren'Py statements, so it requires further processing to determine what Ren'Py statement(s) need(s) to be generated
    EMPTY = -1
    NONE = 0
    SAY = 1
    SHOW = 2
    SCENE = 3
    PLAY = 4
    VOICE = 5
    SOUND = 6
    CHROBJ = 7 # Character Object 'define nm = Character(name='Name', ...)'
    IMAGE = 8
