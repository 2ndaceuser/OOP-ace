class ml_Hero:
    def __init__(self, name, role, dmg_type):
        self.name = name  
        self.role = role  
        self.dmg_type = dmg_type 
    def describe(self):
        return f"{self.name} is a {self.role} hero."
    def __str__(self):
        return f"{self.name} is a {self.role} and deals {self.dmg_type} damage."
        
s1 = ml_Hero("Nolan", "Jungler/Assassin", "Physical Type")
s2 = ml_Hero("Benedetta", "Assassin/Fighter", "Physical Type")
s3 = ml_Hero("Vexana", "Mage", "Magic Type")
s4 = ml_Hero("Claude", "Marksman", "Physical Type")
s5 = ml_Hero("Minotaur", "Tank/Roam/Support", "Physical & True Type")

answer = str(input("Mobile Legends | press any key to enter: "))
print(f'''{answer}\nUsers Activity\nEnter game\nloading screen...\nEnter Lobby, Classic and start the game (10/10)
\nChoose your Hero...\n{s1.describe()}\n{s2.describe()}\n{s3.describe()}\n{s4.describe()}\n{s5.describe()}
\nPlayers locked on heroes:\nS1: {s1}\nS2: {s2}\nS3: {s3}\nS4: {s4}\nS5: {s5}''')
    
''' I Encoded here the Class Definition (`ml_Hero`): The class `ml_Hero` is created to represent a hero in a game. 
Each hero has three characteristics: name, role, and dmg_type

Second, I also include the Constructor (`__init__` method): When a new hero is created,
the `__init__` method is automatically 
called to set the hero's `name`, `role`, 
and `dmg_type` attributes based on the information given.

Describe Method (`describe`): This method returns a simple description of the hero,
mentioning their name and role.
 For example, "Nolan is a Jungler/Assassin hero."

String Representation (`__str__` method): When you print the hero object, 
this method is called to return a more detailed description of the hero, including their name,
role, and the type of damage they deal.
 For example, "Nolan is a Jungler/Assassin and deals Physical Type damage."

Hero Instances: Five different hero objects are created, each with their own `name`, `role`, and `dmg_type`.

User Interaction: The program prompts the user to press any key to start, and then simulates game activity '''