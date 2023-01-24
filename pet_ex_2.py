from human_ex_1 import Human
class Pet:
    def init(self, name, type, favorite_food):
        self.name = name;
        self.type = type;
        self.favorite_food = favorite_food;

    def __str__(self):
        return f'{self.type.capitalize()} called {self.name} that loves {self.favorite_food}.'


class HumanWithPet:
    def init(self, firstname, lastname, date_of_birth, pets=[]):
        Human.init(self, firstname, lastname, date_of_birth)
        self.pets = pets
