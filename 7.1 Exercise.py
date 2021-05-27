'''
#Given the below class:
# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
'''


class Cat:
    species = 'Animal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Pussy', 5)
cat2 = Cat('Sussy', 8)
cat3 = Cat('Mussy', 3)


def findoldest():
    if cat1.age > cat2.age and cat1.age > cat3.age:
        print(f'The oldest cat is {cat1.age} years old.')
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        print(f'The oldest cat is {cat2.age} years old.')
    else:
        print(f'The oldest cat is {cat3.age} years old.')


findoldest()

'''
# One of the best solution is given below.
'''

class Cat:
    species = 'Animal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Cat object with 3 cats
pussy = Cat('Pussy', 7)
mussy = Cat('Mussy', 10)
sussy = Cat('Sussy', 6)

# Find the oldest cat
def find_oldest_cat(*args):
    return max(args)

print(f'The oldest cat is {find_oldest_cat(pussy.age,mussy.age,sussy.age)} years old.')
