class hero_name:
    def __init__(self,name,role,b_attack):
        self.name = name
        self.role = role
        self.b_attack = b_attack

p1 = hero_name("layla", "markmans", "long range")
print(f"Name: {p1.name} \nRole: {p1.role} \nBasic Attack: {p1.b_attack}")
