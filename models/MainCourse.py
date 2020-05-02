from models import Condition
from models.AbstractDish import AbstractDish


class MainCourse(AbstractDish):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients,
                 specifications, condition, side_dish=None, meat=None, sauce=None):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients,
                         specifications, condition)
        self.side_dish = side_dish
        self.meat = meat
        self.sauce = sauce



