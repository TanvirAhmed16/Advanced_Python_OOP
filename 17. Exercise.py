'''
#1 Add another Cat

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []

#3 Instantiate the Pet class with all your cats use variable my_pets

#4 Output all of the cats walking using the my_pets instance
'''


class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Adding another cat.
class Suzzy(Cat):
    def sing(self, sound):
        return f'{sound}'


# 2 Creating 3 cat instance.
# pussy = Cat('Pussy', 5)
# mussy = Cat('Mussy', 10)
# sussy = Cat('Sussy', 8)

my_cats = [Simon('Simon', 8), Sally('Sally', 10), Suzzy('Suzzy', 5)]

# 3 Instantiating Pet class with all my cats using variable my_pets.

my_pets = Pets(my_cats)

# 4 Outputting all of the cats walking using the my_pets instance.
my_pets.walk()
