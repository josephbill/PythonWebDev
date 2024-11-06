class Cat:
    def make_sound(self):
        print("meows")

class Dog:
    def make_sound(self):
        print("barks")


def animal_sound(animalObject):
    animalObject.make_sound()

cat = Cat()
dog = Dog()

animal_sound(cat)
animal_sound(dog)


class Animal:
    def make_sound(self):
        print("animal sound")

class Cat1(Animal):

    def make_sound(self):
        print("cat1 sound : meow")
    def diet(self):
        print("this is the diet")

cat1 = Cat1()
cat1.make_sound()
