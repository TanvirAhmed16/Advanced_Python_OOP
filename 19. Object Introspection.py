'''
# Code introspection in Python - Introspection is an ability to determine the type of an object at runtime.
  Everything in python is an object. Every object in Python may have attributes and methods. By using introspection,
  we can dynamically examine python objects. Code Introspection is used for examining the classes, methods, objects,
  modules, keywords and get information about them so that we can utilize it. Introspection reveals useful information
  about your program’s objects. Python, being a dynamic, object-oriented programming language, provides tremendous
  introspection support.
--> In simple words by using introspection we can see what we have access to for an object.
    We need to use dir() function to use introspection.
'''

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged In.')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)  # We can also do te same like.
        # User.__init__(self, email)

        self.name = name
        self.power = power

    def attack(self):
        User.sign_in(self)
        print(f'{self.name} is attacking with the power of {self.power}.')

wizard1 = Wizard('Tanvir', 25, 'tanvirahmed1627@gmail.com')
print(dir(wizard1))

my_lisy = [1, 2, 3, 'Tanvir']
print(dir(my_lisy))