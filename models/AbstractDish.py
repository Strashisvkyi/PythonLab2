from models import Condition


class AbstractDish:

    def __init__(self, price_in_UAH=0.0, mass_In_grams=0, time_for_cooking_in_minutes=0, name_of_dish=None, ingredients=None, specifications=None, condition=Condition.Coldprice_in_UAH):
        self.price_in_UAH = price_in_UAH
        self.mass_In_Grams = mass_In_grams
        self.time_for_cooking_in_minutes = time_for_cooking_in_minutes
        self.name_of_dish = name_of_dish
        self.ingredients = ingredients
        self.specifications = specifications
        self.condition = condition


    def __del__(self):
        print('deleted ' + self.__class__.__name__)
        return







