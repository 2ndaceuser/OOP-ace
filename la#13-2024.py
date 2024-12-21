class Animal:
    def __init__(self, name, type):
        pass
       
class Fish(Animal):
    def __init__(self, name, type):
        super().__init__(name,type)
        self.name = name
        self.type = type
        self.can_swim = True
   
    def describeFish(self):
        print (f"The {self.name} fish is a type of {self.type} animal and he can swim, {self.can_swim}.")
       
       
Tilapia = Fish("Tilapia", "Aquarius")
Tilapia.describeFish()
#print(f"That is {Tilapia.can_swim}.")