from models import Condition
from models.AbstractDish import AbstractDish


class Soup(AbstractDish):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, consistence='liquid'):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition)
        self.consistence = consistence

