class NamedObject(object):
    def __init__(self, name):
        self.name = name

    def special_function(self):
        print "I am not being overwritten"

    def text(self):
        print "I am a named object"


class Car(NamedObject):
    def __init__(self, weight, color, transmission, name):
        self.weight = weight
        self.color = color
        self.transmission = transmission
        self.speed = 0
        super(Car, self).__init__(name)

    def __repr__(self):
        return "Car: {0}".format(self.name)

    def accelerate(self):
        self.speed += 10

    def text(self):
        print "Baylee is a new sheriff in town"


class Person(NamedObject):
    def __init__(self, name, age):
        self.age = age
        self.cars = []
        super(Person, self).__init__(name)

    def __repr__(self):
        return "Person: {0}".format(self.name)





