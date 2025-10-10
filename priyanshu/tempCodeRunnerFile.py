class Student:
    def __init__(self, name, marks):
        self.__name = name      # private
        self.__marks = marks    # private

    # getter for name
    def get_name(self):
        return self.__name

    # setter for name
    def set_name(self, name):
        self.__name = name

    # getter for marks
    def get_marks(self):
        return self.__marks

    # setter for marks
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

# Usage
s = Student("Rahul", 85)
print(s.get_name(), s.get_marks())

s.set_marks(95)   # controlled modification
print(s.get_name(), s.get_marks())

s.set_marks(150)  # invalid input handled
