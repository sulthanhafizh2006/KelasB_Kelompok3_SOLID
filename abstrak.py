from abc import ABC, abstractmethod
class Hewan(ABC):
    @abstractmethod
    def makan(self):
        pass
class BisaTerbang(ABC):

    @abstractmethod
    def terbang(self):
        pass