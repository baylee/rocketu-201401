class Apartment(object):
    def __init__(self, unit, rent, sqft, num_bedrooms, num_bathrooms):
        self.unit = unit
        self.rent = rent
        self.sqft = sqft
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.renters = []

    def __repr__(self):
        return self.unit

    def is_full(self):
        # if the number of renters < number of bedrooms, return false, else return true (full)
        if len(self.renters) < int(self.num_bedrooms):
            return False
        else:
            return True