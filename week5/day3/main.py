from building import Building
from apartment import Apartment
from person import Person

print "Welcome to the building manager application!"
response = raw_input("Would you like to add a (b)uilding, (a)partment, (r)enter, or (q)uit? ")

while response != "q":
    if response == "b":
        name = raw_input("What is the name of this building? ")
        address = raw_input("What is the address? ")
        num_floors = raw_input("How many floors are in the building? ")
        doorman = raw_input("Does the building have a doorman? (t/f)")
        if doorman == "t":
            doorman = True
        else:
            doorman = False
        building = Building(name=name, address=address, num_floors=num_floors, doorman=doorman)
        print "Thanks for adding building {0}".format(building)

    if response == "a":
        unit = raw_input("What is the unit number? ")
        rent = raw_input("What is the monthly rent? ")
        sqft = raw_input("How many sq feet are in the apartment? ")
        num_bedrooms = raw_input("How many bedrooms does it have? ")
        num_bathrooms = raw_input("How many bathrooms does it have? ")
        apartment = Apartment(unit=unit, rent=rent, sqft=sqft, num_bedrooms=num_bedrooms, num_bathrooms=num_bathrooms)
        try:
            building.apartments[unit] = apartment
            print "Thanks for adding unit {0} to building {1}".format(apartment.unit, building.name)
        except NameError:
            print "You have to add a building first"

    if response == "r":
        name = raw_input("What is the renter's name? ")
        age = raw_input("What is the renter's age? ")
        renter = Person(name=name, age=age)
        if not apartment.is_full():
            apartment.renters.append(renter)
            print "Renter {0} added to apartment {1}".format(renter.name, apartment.unit)
        else:
            print "That apartment is already full"

    response = raw_input("Would you like to add a (b)uilding, (a)partment, (r)enter, or (q)uit? ")








