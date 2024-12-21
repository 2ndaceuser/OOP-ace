
class Appliance:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("operating")
    def info(self):
        print(f"The brand is {self.brand} and the model is {self.model}")
   
class washingmachine(Appliance):
    def operate(self):
        print("washing clothes")
       
class refrigerator(Appliance):
    def operate(self):
        print("keeping food cold")
       
class microwave(Appliance):
    def operate(self):
        print("heating food")
       
wm = washingmachine("opent", "hanabishi")
rg = refrigerator("snake", "toyota")
mw = microwave("gg", "house")

for Appliance in [wm, rg, mw]:
    Appliance.operate()
    Appliance.info()
