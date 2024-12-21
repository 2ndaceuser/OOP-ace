class Birthday:
    def __init__(self, foods):
        self.foods = foods
    def special_dish(self):
        print("Special Dish: lumpia, pancit, ice cream, etc...")
        self.__secret_dish()
    def __secret_dish(self):
        print(self.foods)
       
food = Birthday("Different Party Themes: Hollywood, anime")
food.special_dish()
