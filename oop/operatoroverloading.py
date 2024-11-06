"""
Feature in python that allows us to redefine the behaviour of operators like + - * for objects of user
defined classes.


"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # operator overloading +
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector ({self.x},{self.y})"


v1 = Vector(3,4)
v2 = Vector(1,2)

v3 = v1 + v2

print(v3)