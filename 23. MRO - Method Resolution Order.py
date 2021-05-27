'''
# Method Resolution Order - The Python Method Resolution Order defines the class search path used by Python to search
  for the right method to use in classes having multi-inheritance.
# In python, method resolution order defines the order in which the base classes are searched when executing a method.
  First, the method or attribute is searched within a class and then it follows the order we specified while
  inheriting. This order is also called Linearization of a class and set of rules are called MRO(Method Resolution
  Order). While inheriting from another class, the interpreter needs a way to resolve the methods that are being
  called via an instance. Thus we need the method resolution order. For Example
'''

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num)

print(D.__mro__)

'''
###### That's all from OOP in Python. Practice more. Happy Coding...#####
'''