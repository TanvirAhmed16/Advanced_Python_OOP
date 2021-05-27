'''
# What is Polymorphism : The word polymorphism means having many forms. In programming, polymorphism means same
    function name (but different signatures) being uses for different types.
'''


class User():
    def sign_in(self):
        print('Logged In.')

    def attack(self):
        print('Do nothing.')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        # User.attack(self)
        print(f'{self.name} attacking with power of {self.power}.')
        return 'Attack Successful.'


class Archer(User):
    def __init__(self, name, no_of_arrow):
        self.name = name
        self.no_of_arrow = no_of_arrow

    def attack(self):
        print(f'{self.name} attacking with arrow. Arrows left: {self.no_of_arrow}.')
        return 'Attack Successful.'


'''
# Here we can see we have methods with same name in our all class. Yet they gives us different output.
'''
wizard1 = Wizard('Tan', 100)
archer1 = Archer('Tanvir', 30)
print(wizard1.attack())
print(archer1.attack() + '\n')

'''Here User's attack function is not executing as it is being override by the attack method of Wizard and Archer class.
We can also make a default function to call this method.
Let's say we also want to access attack method in our super class. Then we need mention that method using class as 
shown in line 21.
'''


def call_attack(char):
    char.attack()


call_attack(wizard1)
call_attack(archer1)
print('\n')

# We can also do the same using a for loop.

for char in [wizard1, archer1]:
    char.attack()
print('\n')


'''
# Now demonstrating some example from some websites.
'''
# Example of inbuilt polymorphic functions :

# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))

# Examples of used defined polymorphic functions :

# A simple Python function to demonstrate Polymorphism

def add(x, y, z=0):
    return x + y + z


# Driver code
print(add(2, 3))
print(add(2, 3, 4))

# Polymorphism with class methods:

class Bangladesh():
    def capital(self):
        print('Capital of Bangladesh is Dhaka.')

    def language(self):
        print('Bangla is used as national language.')


class India():
    def capital(self):
        print('Capital of India is Delhi.')

    def language(self):
        print('Hindi is used as national language.')

bd = Bangladesh()
ind = India()
for country in (bd, ind):
    country.capital()
    country.language()


'''
# Polymorphism with Inheritance and Polymorphism with a Function and objects is already shown in our first example.
'''