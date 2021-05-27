class PlayerCharacter:
    # We can have Class Object Attributes which are static. We can use them anywhere like...
    membership = True

    def __init__(self, name, age):
        if (self.membership):  # We could have written if (PlayerCharacter.membership):
            self.name = name  # Attributes which are dynamic with every object.
            self.age = age

    def shout(self):
        print(f'My name is {self.name}, I am {self.age} years old.')
        # We can not use here {PlayerCharacter.name} as name is not a class object attribute. It is basically defined
        # in our constructor __init__ function.

    def run(self, Hello):
        # print('run')
        return 'Done'


player1 = PlayerCharacter('Tan', 25)
player2 = PlayerCharacter('Tanvir', 28)

print(player1.membership)
print(player2.membership)

print(player1.shout())
print(player2.shout())

print(player1.run('Hello'))
