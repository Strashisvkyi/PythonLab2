from models.Dessert import Dessert


class Muffin(Dessert):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, persentage_of_sugar, filling=None):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, persentage_of_sugar)
        self.filling = filling


