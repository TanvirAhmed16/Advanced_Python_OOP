'''
# Abstraction means hiding the complexity and only showing the essential features of the object. So in a way,
  Abstraction means hiding the real implementation and we, as a user, knowing only how to use it.
  Abstraction in Python is achieved by using abstract classes and interfaces.
  For more go to https://www.geeksforgeeks.org/abstract-classes-in-python/
# Don't know why Andrei said in his tutorial that we shouldn't use double __ to make an attribute private, insted he
  said we can use single _ to make an attribute private where we have seen that we can use double __ to make an
  attribute private. We can also do the same for method. Showing below.
'''


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __run(self):
        print(f'{self.name} needs to run.')


p1 = PlayerCharacter('Tan', 25)
print(p1._PlayerCharacter__run())

p2 = PlayerCharacter('Tanvir', 30)
#print(p2.__run())  # This will give us an error as we can not access a private method like this.


'''
# An proper example is given below.
'''
# Python program showing
# abstract class cannot
# be an instantiation
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


c = Animal()