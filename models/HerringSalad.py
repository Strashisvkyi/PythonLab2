from models.Salad import Salad


class HerringSalad(Salad):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, salad_dressing, persentage_of_salt=0):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients, specifications, condition, salad_dressing)
        self.persentage_of_salt = persentage_of_salt

