# constructor overloading is enabled in python using the concept of default arguments
# class X:
#     def __init__(self,name,dob="20/11/2921"):
#         self.name = name
#         self.dob = dob
# x1 = X("namex")
# x2 = X("namex","4/23/2032")
#
# print(x1.name)
# print(x2.name)

class Rectangle:
    def __init__(self, length,width=None):
        if width is None:
            width = length # using the length value to also represent my width if no width is provided , meaning its a square
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


square = Rectangle(5)
rectangle = Rectangle(5,10)
print("Square area" , square.area())
print("Rectangle area" , rectangle.area())