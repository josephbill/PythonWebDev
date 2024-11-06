"""
Class methods operate on the class itself rather than instances of the class
they are marked using the @classmethod decorator and take the cls value as a parameter , represent the class
- used for utility functionalities attached to the class
Class attributes are attributes belonging to the class and not a specific instance of the class
"""
from jedi.debug import speed


class Dog:
    # class attributes : simply define them outside the methods
    species = "German Shepherds"
    dog_count = 0 # class attribute that keeps track of my objects created from this blueprint
    def __init__(self, name):
        self.name = name
        Dog.dog_count += 1

    def make_sound(self):
        return f"The species {self.species}"

    @classmethod
    def get_dog_count(cls):
        return cls.dog_count


dog1 = Dog("Buddy")
print(dog1.name)
print(dog1.species)
dog2 = Dog("Rex")
print(dog2.name)
print(dog2.species)
# class methods are accessed by referencing the class name followed by the method name
print(Dog.get_dog_count())


### if functions carries self as a parameter :: instance/object method
### if function carries cls as a parameter :: belongs to the class i.e. accessible from all instances/objects
### if function has no cls, or self parameter inside a class then it has to be denoted with the @staticmethod
### decorator.
### instance attributes : attributes belong to methods
### class attributes : attributes belonging to the class i.e. all instances of the class.