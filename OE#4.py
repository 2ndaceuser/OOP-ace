class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}! {target.name}'s remaining health: {target.health}")

    def defend(self, damage):
        self.health -= max(0, damage - 5)  # Reduces damage by 5
        print(f"{self.name} defends! Remaining health: {self.health}")

    def special_move(self, target=None):
        pass

class Warrior(Character):
    def special_move(self):
        self.power *= 2
        print("Warrior uses Shield Bash!")

class Mage(Character):
    def special_move(self, target):
        target.health -= 188
        print("Mage casts Fireball!")

class Archer(Character):
    def special_move(self, target):
        target.health -= self.power
        print("Archer shoots Piercing Arrow!")

class Monster(Character):
    def special_move(self):
        self.health += 40
        print("Monster roars and gains health!")

# Simulating a battle
warrior = Warrior("Warrior", 100, 20)
mage = Mage("Mage", 80, 15)
archer = Archer("Archer", 90, 10)
monster = Monster("Monster", 120, 5)

characters = [warrior, mage, archer, monster]

for character in characters:
    if isinstance(character, (Mage, Archer)):
        character.special_move(monster)  
    else:
        character.special_move()
    character.attack(monster)
    monster.defend(character.power)  # Monster defends against the attack