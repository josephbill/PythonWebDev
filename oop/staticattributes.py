"""
Static methods
are methods that belong to the class but dont operate on the class or its instances directly
they are marked with the decorator function called @staticmethod , they dont take in any cls or self parameter
- used when you need a utility function that is logically related to the class but doesnt need to access class or
instance data
"""

class MathC:
    def anymethod(self,x,y):
        x = MathC.add(x,y)
        return x

    @staticmethod
    def add(x,y):
        return x + y


# use a static method
print(MathC.add(7,8))
math1 = MathC()
print(math1.anymethod(10,9))
