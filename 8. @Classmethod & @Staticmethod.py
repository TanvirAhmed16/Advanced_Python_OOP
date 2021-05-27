'''
# @Classmethod & @Staticmethod
    Basically they both works like a decorator.
--> Class Methods: Can access limited methods in the class. Can modify class specific details.
    Class methods don't need self as an argument, but they do need a parameter called cls. This stands for class,
    and like self, gets automatically passed in by Python. Class methods are created using the @classmethod decorator.
--> Static Methods: Cannot access anything else in the class. Totally self-contained code.
    Static methods are methods that are related to a class in some way, but don't need to access any class-specific
    data. You don't have to use self, and you don't even need to instantiate an instance,you can simply call your
    method.
'''


class PlayerCharacter():
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'My name is {self.name}.')

    # Decorator
    @classmethod
    def adding_things(cls, num1, num2):
        return (num1 + num2)  # cls basically indicates the class.

    # Instantiating using class method.
    @classmethod
    def creating_things(cls, num):
        return cls('Tanvir', num)

    @staticmethod
    def multiply_things(num1, num2, num3):
        return num1 * num2 * num3


player1 = PlayerCharacter('Tan', 25)

print(player1.name)
print(player1.adding_things(15, 10))

# We can even instantiate an object using the class method as it works with the class.
player2 = PlayerCharacter.creating_things(20)
print(player2.name, player2.age)

print(f'The answer of the multiplication is {PlayerCharacter.multiply_things(2, 3, 4)}.\n')

'''
# Another example is given below.
'''

from datetime import date


class Person():
    # Instance Method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class Method
    @classmethod
    def birth_date(cls, name, year):
        return cls(name, date.today().year - year)

    # Static Method
    @staticmethod
    def is_adilt(age):
        return age > 18


a = Person('Tapu', 17)
b = Person.birth_date('Tanvir Ahmed', 1992)

print(f'Name: {a.name}, Is he adult? -- {Person.is_adilt(a.age)}')
print(f'Name: {b.name}, Is he adult? -- {Person.is_adilt(b.age)}')
