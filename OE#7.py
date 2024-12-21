class TekkenCharacter:
    def __init__(self, name, ability):  # Correct constructor name
        self.name = name
        self.ability = ability

    def introduce(self, function):  # Decorator function
        def wrapper():
            print("Introducing.....")
            function()
            print("This Character is amazing!!!!")
        return wrapper


# Create the TekkenCharacter instance
charac = TekkenCharacter("Law", "Combo Damage")

# Decorate the character_intro function
@charac.introduce
def character_intro():
    print(f"I am {charac.name} and my ability is {charac.ability}")


# Call the decorated function
character_intro()