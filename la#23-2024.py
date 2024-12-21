class AnimeCharacter:
    def __init__(self, name, ability):
        self .__name = name
        self.ability = ability
    def anime(self, new_func):
        def opening(*args, **kwargs):
            print("--- Introducing... ---")
            new_func(*args, **kwargs)
            print("--- This character is amazing! ---")
            print("")
        return opening
power = AnimeCharacter("name", "ability")

@power.anime
def naruto(sign, name, ability):
    print(f"{sign} anime character: {name}, abilities: {ability} ")

@power.anime
def denji (sign, name, ability):
    print(f"{sign} anime character:{name}, abilities: {ability}")

   
naruto(">>", "naruto", "9 tails")
denji(">>", "denji", "chainsaw devil" )