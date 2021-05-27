'''
# We need to create a list in the class Superlist() where we will be able to do all the normal operation on a list
  and we need to modify the dunder __len__() method also that will return nothing but 1000.
'''

class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()
super_list1.append(5)
super_list1.insert(0, 4)
print(super_list1)
print(super_list1[0])
print(super_list1.__len__())
print(isinstance(super_list1, SuperList))
print(isinstance(list, object))



