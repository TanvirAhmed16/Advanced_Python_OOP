'''
# Let's create our own class and object.
# We need to remember, while creating a class, it's naming convention should be in camel case and it can't be plural.
# WHen we need to access a method, we have to use () brackets.
'''


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'Done'


player1 = PlayerCharacter('Tan', 25)
player2 = PlayerCharacter('Tanvir', 28)

print(player1.name, 'you are', player1.age, 'years old.')
print(player2.name, 'you are', player2.age, 'years old.')

print(player1.run())  # Here it will give us a None value as there is no return type.

print(player2.run)  # This will happen if we don't use () brackets while accessing a method of a class.

print(player1)
print(player2)  # THis will show us the memory location where this two objects are stored after created.

'''
# We can also add property of a played or object. Like
'''
player2.attack = 50

print(player2.attack)
print(player1.attack)
