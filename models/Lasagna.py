from models.MainCourse import MainCourse


class Lasagna(MainCourse):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients,
                 specifications, condition, side_dish, meat, sauce, recipe_used=None):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients,
                         specifications, condition, side_dish, meat, sauce)
        self.recipe_used = recipe_used




