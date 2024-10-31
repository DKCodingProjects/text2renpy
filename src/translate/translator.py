from abc import ABC, abstractmethod

class Translator(ABC):
    def __init__(self):
        # add variables
        pass
    
    @abstractmethod
    def translate_except(self, err: Exception):
        raise Exception('An error occured in {0} while translating content({1})'.format(self.__class__.__name__, f"{type(err).__name__}: {err}"))
    
    @abstractmethod
    def translate(self, text, attribs):
        pass