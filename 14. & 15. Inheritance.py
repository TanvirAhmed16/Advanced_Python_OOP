'''
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
'''

class User():
    def sign_in(self):
        print('Logged In.')

class Wizerd(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} attack with the power of {self.power}.')

class Archer(User):
    def __init__(self, name, no_of_archer):
        self.name = name
        self.no_of_archer = no_of_archer

    def attack(self):
        print(f'{self.name} attack with archer: archer left - {self.no_of_archer}.')

wizerd1 = Wizerd('Marlin', 50)
print(wizerd1)
print(wizerd1.sign_in())  # Here we can see,though sign_in() is not a method of Wizerd class. We still can access it.

wizerd2 = Wizerd('Tanvir', 100)
print(wizerd2.sign_in())
print(wizerd2.attack())

archer1 = Archer('Tan', 200)
print(archer1.sign_in())
print(archer1.attack())
print('\n')
'''
# Python gives us useful tools to check whether anything is an instance of a class or not.
# Syntax - isinstance(instance, class)
'''
print(isinstance(wizerd1, Wizerd))
print(isinstance(wizerd2, User))  # As Wizerd class is a sub class of User.
print(isinstance(wizerd2, object))  # As everything in Python is an object. So everything in python inherite from
# object base class. That's why it gives us true value.
print('\n')
'''
# Another example - Single Inheritance.
'''

class Vehicle():
    def __init__(self, name, cost, mileage):
        self.name = name
        self.cost = cost
        self.mileage = mileage

    def show_vehicle_details(self):
        print(f'Vehicle Brand: {self.name}.')
        print(f'Cost of the vehicle: {self.cost} $.')
        print(f'Mileage of the vehicle: {self.mileage} kmpl.')

class Car(Vehicle):
    def show_car_details(self):
        print(f'My brand name is {self.name}.')

car1 = Car('Mercedez', 20000, 20)
print(car1.show_vehicle_details())
print('\n')
'''
# Overriding the __init__ method or creating child class constructor.
'''
class Vehicle():
    def __init__(self, name, cost, mileage):
        self.name = name
        self.cost = cost
        self.mileage = mileage

    def show_vehicle_details(self):
        print(f'Vehicle Brand: {self.name}.')
        print(f'Cost of the vehicle: {self.cost} $.')
        print(f'Mileage of the vehicle: {self.mileage} kmpl.')

class Bus(Vehicle):
    def __init__(self, name, cost, mileage, tyres, hp):
        super().__init__(name, cost, mileage)
        self.tyres = tyres
        self.hp = hp

    def show_bus_details(self):
        print(f'My brand name is {self.name}.')
        print(f'My number of tyres are: {self.tyres}.')
        print(f'My engine HorsePower is: {self.hp}.')

bus1 = Bus('Mercedez', 20000, 20, 10, 2000)
print(bus1.show_bus_details(), bus1.show_vehicle_details())
print('\n')

'''
# Now demonstrating Multiple Inheritance.
'''

class Parent1():
    def assign_string_one(self, str1):
        self.str1 = str1

    def show_string_one(self):
        return self.str1


class Parent2():
    def assign_string_two(self, str2):
        self.str2 = str2

    def show_string_two(self):
        return self.str2

class Child(Parent1, Parent2):
    def assign_string_three(self, str3):
        self.str3 = str3

    def show_string_three(self):
        return self.str3

child1 = Child()
child1.assign_string_one('I am string of Parent 1.')
child1.assign_string_two('I am string of Parent 2.')
child1.assign_string_three('I am string of Child.')

print(child1.show_string_one())
print(child1.show_string_two())
print(child1.show_string_three())
print('\n')

'''
# Now demonstrating Multilevel Inheritance.
'''
class Parent():
    def assign_name(self, name):
        self.name = name

    def show_name(self):
        return self.name


class Child(Parent):
    def assign_age(self, age):
        self.age = age

    def show_age(self):
        return self.age


class GrandChild(Child):
    def assign_gender(self, gender):
        self.gender = gender

    def show_details(self):
        return self.name, self.age, self.gender

grandchild = GrandChild()
grandchild.assign_name('Tanvir.')
grandchild.assign_age(25)
grandchild.assign_gender('Male')
print(grandchild.show_details())