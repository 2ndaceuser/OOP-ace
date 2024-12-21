

class dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Dog sound is {self.name} ")
    
class cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Cat sound is {self.name}")
    
class bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Bird sound is {self.name}")
        
class fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Fish sound is {self.name}")

def animal_sounds(animal):
    animal.speak()
        
ds = dog("Bark!")
cs = cat("Meow!")
bs = bird("Chirp!")
fs = fish("...")



animal_sounds = [ds, cs, bs, fs]
count = 0
while count < len(animal_sounds):
    animal_sounds[count].speak()
    count += 1
