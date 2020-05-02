from models import DegreeOfMeatDoneness
from models.MainCourse import MainCourse


class Goulash(MainCourse):
    def __init__(self, price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients,
                 specifications, condition, side_dish, meat, sauce, pungency_level=None, degree_of_meat_doneness=DegreeOfMeatDoneness.Rare):
        super().__init__(price_in_UAH, mass_In_grams, time_for_cooking_in_minutes, name_of_dish, ingredients,
                         specifications, condition, side_dish, meat, sauce)
        self.degree_of_meat_doneness = degree_of_meat_doneness
        self.pungency_level = pungency_level


