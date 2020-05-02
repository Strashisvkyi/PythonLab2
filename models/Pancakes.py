from models.Dessert import Dessert


class Pancakes(Dessert):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, persentage_of_sugar, numberOfPancakes=0, syrup=None):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, persentage_of_sugar)
        self.numberOfPancakes = numberOfPancakes
        self.syrup = syrup


