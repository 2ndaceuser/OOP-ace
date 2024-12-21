class Adobo: 
    def __init__(self, main_ingredient, Onion, Soysouce, Pepper):
        self.main_ingredient = main_ingredient
        self._Onion = Onion
        self._Soysouce = Soysouce
        self.__Pepper = Pepper

    def __str__(self):
        return f"My favorite adobo has {self.main_ingredient}, {self._Onion}, {self._Soysouce} and {self.__Pepper}." 
    
    def doesithavePepper(self, age):
        self.age = age
        if age <= 18:
            return self.__Pepper
        else: 
            return "The dish doesn't have pepper"
    def updatePepper(self, new, ex):
        if ex == "Yes":
            self.__Pepper = new
            return "Update Succesfully"
        else:
            return "Sorry!"
            
adobo1 = Adobo("Chiken", "onion", "Soysouce", "Pepper")

print(adobo1.updatePepper("no pepper", "Yes"))

print(adobo1.doesithavePepper(20))
