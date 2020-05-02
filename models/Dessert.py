from models import Condition
from models.AbstractDish import AbstractDish


class Dessert(AbstractDish):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, persentage_of_sugar=0):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition)
        self.persentage_of_sugar = persentage_of_sugar

