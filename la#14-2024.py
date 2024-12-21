class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describeSpiderman(self):
        print(f"name: {self.name} - age: {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
    
    

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
        
   

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
    

sp1 = Tobey("Tobey", 30, "spiderman")
sp2 = Andrew("Andrew", 21, "amazing spiderman")
sp3 = Tom("Tom", 20, "spiderman")

sp1.describeSpiderman()
sp2.describeSpiderman()
sp3.describeSpiderman()

print(sp1.name.upper(),"-", sp1.movieTitle.upper())
print(sp2.name.upper(),"-", sp2.movieTitle.upper())
print(sp3.name.upper(),"-", sp3.movieTitle.upper())
