#LA12
class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
       
   
    def toyDetail(self):
        print (f"This toy is a {self.name} toy and it has a price of {self.price}PHP. ")
           
class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
       
play = Toy("Car", 360)


play.toyDetail()
