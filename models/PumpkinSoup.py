from models.Soup import Soup


class PumpkinSoup(Soup):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, consistence, countryOfOrigin=None):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, consistence)
        self.countryOfOrigin = countryOfOrigin
