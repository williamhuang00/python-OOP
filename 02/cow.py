from animal import Animal

class Cow(Animal):
    def __init__(self, name):
        self.name = name
        self.species = 'cow'

my_cow = Cow('bessie')
my_cow.eat()
my_cow.sleep()