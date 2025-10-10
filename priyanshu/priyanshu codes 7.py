# Single Inheritance Example

class Animal:   # Base class
    def speak(self):
        print("Animals can make sounds.")

class Dog(Animal):  # Derived class
    def bark(self):
        print("Dog barks: Woof! Woof!")

# Using single inheritance
d = Dog()
d.speak()   # Inherited from Animal
d.bark()    # Defined in Dog
