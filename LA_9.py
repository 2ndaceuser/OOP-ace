class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"This car is a {self.brand}."

my_car = Car("Tesla")
print(my_car)

del my_car

print(my_car)  
