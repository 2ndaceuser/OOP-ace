class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
   
    def describePhone(self):
        print (f"This {self.brand} is a type of {self.model} but a newer versionphone model")
           
class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)
       
     

PhoneZ = Android("SAMSUNG GT", "SAMSUNG GALAXY")

PhoneZ.describePhone()