from abc import ABC, abstractmethod

class Proxy(ABC):
    
    def _get_instance_except(self, instance: object, err: Exception):
        raise Exception('An error occured in {0} while getting instance of \'{1}\' ({2})'.format(self.__class__.__name__, instance.__class__.__name__, f"{type(err).__name__}: {err}"))

    @abstractmethod
    def get_instance(self):
        pass