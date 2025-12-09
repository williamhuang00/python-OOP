class Animal:
    def __init__(self, name: str, species: str, sound: str):
        self.name = name
        self.species = species
        self.sound = sound
    
    def eat(self):
        print('it eats')
    
    def sleep(self):
        print('it sleeps')
