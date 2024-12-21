import abc
from abc import ABC, abstractmethod
#LA#25
class Character(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass
class Batman(Character):
    def __init__(self,name,alias):
        self.name = name
        self.__alias = alias
    @property
    def alias(self):
        return self.__alias

bat = Batman("Bruce Wayne", "Batman")
print(bat.alias)