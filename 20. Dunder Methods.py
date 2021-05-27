'''
# Dunder methods basically allow us to use Python specific functions on objects created through our class.
# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
  Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. Few examples
  for magic methods are: __init__, __add__, __len__, __repr__, __str__ etc.
--> object.__repr__(self)
    Called by the repr() built-in function to compute the “official” string representation of an object.
--> object.__str__(self)
    Called by str(object) and the built-in functions format() and print() to compute the “informal” or nicely
    printable string representation of an object. The return value must be a string object.
--> There are tons of more present in Python here... https://docs.python.org/3/reference/datamodel.html
# We can customize these dunder methods as per our requirement.
'''


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': True
        }

    def __str__(self):
        return self.color

    def __repr__(self):
        return f'Toy\'s Color: {self.color}.'

    def __len__(self):
        return 5

    def __add__(self, other):
        return self.age + other.age

    def __call__(self, *args, **kwargs):
        return 'Calling.'

# When we won't pass any parameter inside an object then Python will automatically execute it's dunder call method.

    def __getitem__(self, item):
        return self.my_dict[item]


toy1 = Toy('Green', 1)
toy2 = Toy('Red', 2)

print(toy1.__str__())
print(toy1.__repr__())
print(len(toy1))
print(toy1.__add__(toy2))
print(toy2())
print(toy1.__getitem__('name'))
