from models.Salad import Salad


class GreekSalad(Salad):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, salad_dressing, freshness_of_vegs_in_percent=0):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, salad_dressing)
        self.freshness_of_vegs_in_percent = freshness_of_vegs_in_percent

