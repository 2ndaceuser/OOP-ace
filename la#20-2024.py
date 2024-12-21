
class Food:
    def __init__(self, main, alpha, beta, charlie):
        self.main = main
        self.__alpha = alpha
        self.__beta = beta
        self.__charlie = charlie
    def __str__(self):
        return f"My favorite food is {self.main} and it's ingredients is {self.__alpha}, {self.__beta}, {self.__charlie}"
    def may_charlie_ba(self):
        return self.__charlie
    def may_alpha_ba(self):
        return self.__alpha
    def may_beta_ba(self):
        return self.__beta
       
egg_main = Food ("Leche flan", "egg", "evaporated milk","sweetened condensed milk")
egg_main1 = Food ("Adobo", "chicken","soysauce", "garlic")
egg_main2 = Food ("Halo-halo", "crushed ice", "evaporated milk","various ingredients")

print(egg_main.main)
print(egg_main1.may_alpha_ba())
print(egg_main2.may_beta_ba())
print(egg_main.may_charlie_ba())
