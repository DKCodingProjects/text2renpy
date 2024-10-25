from abc import ABC, abstractmethod

class Translator(ABC):
    def __init__(self):
        # add variables
        pass

    @abstractmethod
    def translate(self, text, attribs):
        pass