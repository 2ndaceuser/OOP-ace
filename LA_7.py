class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car = Car("Toyota", "Red")
print(f"Initial color: {car.color}")

car.color = "Blue"
print(f"Updated color: {car.color}")

