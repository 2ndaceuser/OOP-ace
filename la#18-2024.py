
class Food:
    def __init__(self, main, alpha, beta, charlie):
        self.__main = main
        self.__alpha = alpha
        self.__beta = beta
        self.__charlie = charlie
    def __str__(self):
        return f"My favorite food is {self.__main} and it's ingredients is {self.__alpha}, {self.__beta}, {self.__charlie}"
egg_main = Food ("Leche flan", "egg", "evaporated milk","sweetened condensed milk")
egg_main1 = Food ("Adobo", "chicken","soysauce", "garlic")
egg_main2 = Food ("Halo-halo", "Crushed ice", "evaporated milk","various ingredients")
print(egg_main)
print(egg_main1)
print(egg_main2)
