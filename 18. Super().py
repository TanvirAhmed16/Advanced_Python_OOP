'''
# In Python, super() is generally used when we need to access any attribute of a super class from a sub class when
  the sub class already have it's own __init__ constructor.
# The super() function is used to give access to methods and properties of a parent or sibling class. Though we have
  used this before. Let's see again.
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


# wizard1 = Wizard('Tanvir', 25, 'tanvirahmed1627@gmail.com')
# print(wizard1.attack())
'''
# Here though Wizard class inherit User class, still we can't access it's email attribute unless we use super()
  function as Wizard class already have a __init__ constructor. This error will shown.
  __init__() takes 3 positional arguments but 4 were given
'''

wizard2 = Wizard('Tanvir', 25, 'tanvirahmed1627@gmail.com')
print(wizard2.email)
print(wizard2.attack())
