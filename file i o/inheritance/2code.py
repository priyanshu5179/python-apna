gti """ class ParentClass:
    def method(self):
        return "Parent class method"

class ChildClass(ParentClass):
    def method(self):
        return "Child class method"

parent_obj = ParentClass()
child_obj = ChildClass()

print(parent_obj.method())
print(child_obj.method())
"""
# method over writting
class Animal:
    def make_sound(self):
        print("generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("woof")

class Cat(Animal):
    def make_sound(self):
        print("meow")

animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()
dog.make_sound()
cat.make_sound()