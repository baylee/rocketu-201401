class Building(object):
    def __init__(self, address, num_floors, doorman, name):
        self.address = address
        self.num_floors = num_floors
        # Doorman is a boolean
        self.doorman = doorman
        self.name = name
        self.apartments = {}

    def __repr__(self):
        return self.name