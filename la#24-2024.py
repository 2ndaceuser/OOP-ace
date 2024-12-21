from abc import ABC, abstractmethod
class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def introduce(self):
        print(f"I'm {self.name}")
       
class Warrior(GameCharacter):
    def introduce(self):
        print(f"Warrior: {self.name}")
       
class Mage(GameCharacter):
    def introduce(self):
        print(f"Mage: {self.name}")
       
class Archer(GameCharacter):
    def introduce(self):
        print(f"Archer: {self.name}")

class Healer(GameCharacter):
    def introduce(self):
        print(f"Healer: {self.name}")

hero = Warrior("Swings sword!")
hero.introduce()
hero = Mage("Casts a fireball!")
hero.introduce()
hero = Archer("Shoots an arrow!")
hero.introduce()
hero = Healer("Casts healing spell on allies!")
hero.introduce()