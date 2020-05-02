from models.Soup import Soup


class MushroomSoup(Soup):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, consistence, mushroom_type=None):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, consistence)
        self.mushroom_type = mushroom_type
