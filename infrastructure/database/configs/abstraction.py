from abc import ABC, abstractmethod

class AbstractDatabase(ABC):

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError()
    
    @abstractmethod
    def __exit__(self, exc_type, exc_value, exc_tb):
        raise NotImplementedError()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()
