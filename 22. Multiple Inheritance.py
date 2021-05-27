'''
# Let's do some practice of multiple inheritance.
'''


class User():
    def sign_in(self):
        print('Logged In.')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f'{self.name} is attacking with the power of {self.power}.'


class Archer(User):
    def __init__(self, name, no_of_arrows):
        self.name = name
        self.no_of_arrows = no_of_arrows

    def attack(self):
        return f'{self.name} is attacking with {self.no_of_arrows} arrows.'

    def check_arrows(self):
        return f'Arrows Remaining: {self.no_of_arrows}'

    def run(self):
        return f'Fall back to safe zone.'


class Hybrid_Character(Wizard, Archer):
    def __init__(self, name, power, no_of_arrows):
        Archer.__init__(self, name, no_of_arrows)
        Wizard.__init__(self, name, power)
        # super().__init__(name, no_of_arrows)
        # super().__init__(name, power)


'''
# Here we will see though Hybrid_Character inherit it's above all classes, still we are not able to access those
  methods where some attributes are used to complete those methods unless we declare all of the above 
  __init__() constructors.
  ??? Why i am being unable to use super() function???
'''
hc1 = Hybrid_Character('Tanvir', 99, 50)

print(hc1.sign_in())
print(hc1.attack())
print(Archer.attack(hc1))
print(hc1.check_arrows())
print(hc1.run())

