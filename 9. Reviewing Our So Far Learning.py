'''
# So far we have learnt about
    --> Creating Class and Object.
    --> Creating Instance Method.
    --> Creating Class Method.
    --> Creating Static Method.
'''


class NameOfClass():
    class_object_attribute = "Param"

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        pass
        # Code

    @classmethod
    def class_method_name(cls, param1, param2):
        pass
        # Code

    @staticmethod
    def static_method_name(param1, param2, param3):
        pass
        # Code
