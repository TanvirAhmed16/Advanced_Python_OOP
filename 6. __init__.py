'''
# We need to remember that our constructor function gets called every time we instantiate an object.
# So we have a control over how this instantiation happens. For example let's set the player having age below 18
  can not play our game.
# As we have seen before, we can also give default parameters.
'''


class PlayerCharacter:
    # We can have Class Object Attributes which are static. We can use them anywhere like...
    membership = True

    def __init__(self, name='Anonymous', age=0):
        if (age > 18):  # We could have written if (PlayerCharacter.membership):
            self.name = name  # Attributes which are dynamic with every object.
            self.age = age

    def shout(self):
        print(f'My name is {self.name}, I am {self.age} years old.')
        # We can not use here {PlayerCharacter.name} as name is not a class object attribute. It is basically defined
        # in our constructor __init__ function.

    def run(self, Hello):
        # print('run')
        return 'Done'


player1 = PlayerCharacter()
player2 = PlayerCharacter('Tanvir', 12)
player3 = PlayerCharacter('Tanvir Ahmed', 28)

print(player3.shout())
print(player2.shout())  # This will give an error as age is under 18, So the program will not instantiate any object.
print(player1.shout())  # This will give an error as there is no age given, so the program will set the age to 0.
                        # So program will not instantiate any object.
