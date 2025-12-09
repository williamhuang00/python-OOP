from animal import Animal


class Chicken(Animal):
    def __init__(self, name):
        self.name = name
        self.species = 'chicken'

my_chicken = Chicken('mr clucky')

my_chicken.eat()
my_chicken.sleep()

