'''
# Encapsulation in Python - The process of wrapping up variables and methods into a single entity is known as
    Encapsulation. It is one of the underlying concepts in object-oriented programming (OOP). It acts as a protective
    shield that puts restrictions on accessing variables and methods directly, and can prevent accidental or
    unauthorized modification of data. Encapsulation also makes objects into more self-sufficient, independently
    functioning pieces.
# Access modifiers - Access modifiers limit access to the variables and functions of a class. Python uses three types
    of access modifiers; they are - private, public and protected.
--> Public members are accessible anywhere from the class. All the member variables of the class are by default public.
--> Protected members are accessible within the class and also available to its sub-classes. To define a protected
    member, prefix the member name with a single underscore “_”.
--> Private members are accessible within the class. To define a private member, prefix the member name with a double
    underscore “__”.
'''


class PlayerCharacter:
    def __init__(self, name, age, sex):
        self.name = name  # Public
        self._age = age  # Private
        self.__sex = sex  # Protected

    def speak(self):
        print(f'My name is {self.name}, I am {self._age} years old and I am {self.__sex} ')
        return 'Done'


player1 = PlayerCharacter('Tanvir', 25, 'Male')
print(player1.speak())
print(player1.name)
print(player1._age)
print(player1._PlayerCharacter__sex)
#print(player1.__sex)  # This line will give us an error as __sex is a private attribute. So we need to access this in
                      # a specific way given up.
print('\n')


'''
# Now demonstrating a better example where we can access the attributes using set and get method.
'''

class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

ford = Car(200, 'Red')
print(ford.speed)
ford.speed = 300
print(ford.speed)  # As speed is a public attribute, we can modify this using assign new value. So we can prevent this
                   # using encapsulation.
print('\n')


class Vehical:
    def __init__(self, name, speed, color):
        self.__name = name
        self.__speed = speed
        self.__color = color

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_speed(self, speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed

    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color

car = Vehical('Ford', 300, 'Red')

print(f'Car Name: {car._Vehical__name}, Car Speed: {car._Vehical__speed}, Car Color: {car._Vehical__color}')

car.set_name('Mercedes')
car.set_speed(400)
car.set_color('Black')

print(f'Car Name: {car.get_name()}, Car Speed: {car.get_speed()}, Car Color: {car.get_color()}')