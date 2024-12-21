from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Leonardo(NinjaTurtle):
    def __init__(self,name,alias):
        self.name = name
        self.__alias = alias
    @property
    def alias(self):
        return self.__alias


class Michelangelo(NinjaTurtle):

    def __init__(self,name,alias):
        self.name = name
        self.__alias = alias
    @property
    def alias(self):
        return self.__alias


class Donatello(NinjaTurtle):

    def __init__(self,name,alias):
        self.name = name
        self.__alias = alias
    @property
    def alias(self):
        return self.__alias


class Rapheal(NinjaTurtle):

    def __init__(self,name,alias):
        self.name = name
        self.__alias = alias
    @property
    def alias(self):
        return self.__alias



if __name__ == "__main__":

    tur1 = Leonardo("Leonardo", "madog")
    print(tur1.name)