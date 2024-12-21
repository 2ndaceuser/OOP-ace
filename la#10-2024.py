class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    def describeVehicle(self):
        print (f"This {self.brand} is a type of {self.model} model and his fuel type is {self.fuel_type}")
           
class Motor(Vehicle):
    pass
class Car(Vehicle):
    pass

Motorcycle = Motor("Xlr8", "Renix", "Premium")
Sportscar = Car("Speed", "Luxulury", "First")

Motorcycle.describeVehicle()
Sportscar.describeVehicle()
