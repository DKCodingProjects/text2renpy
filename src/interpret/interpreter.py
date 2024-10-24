from abc import ABC, abstractmethod

class Interpreter(ABC):
    def __init__(self):
        # add variables
        pass

    @abstractmethod
    def interpret(self, text, attribs):
        pass