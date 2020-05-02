
class Table:

    def __init__(self, number=0, number_of_seats=0, is_free=True, is_cleen=False):
        self.number = number
        self.number_of_seats = number_of_seats
        self.is_free = is_free
        self.is_cleen = is_cleen

    def __del__(self):
        print('deleted ' + self.__class__.__name__)
        return

    

