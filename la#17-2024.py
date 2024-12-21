class Hero:
    def __init__(self, name, hp, atk_dmg):
        self.name = name
        self.hp = hp
        self.atk_dmg = atk_dmg
    def basic_attack(self, target):
        target.hp = target. hp - self.atk_dmg
moskov = Hero("Moskov", 1000, 200)
tigreal = Hero("Tigreal", 2000, 90)
print(moskov.name, moskov.hp, "HP || ", moskov.atk_dmg, "dmg")
print(tigreal.name, tigreal.hp, "HP || ", tigreal.atk_dmg, "dmg")
moskov.basic_attack(tigreal)
print(tigreal.name, tigreal.hp, "HP || ", tigreal.atk_dmg, "dmg")