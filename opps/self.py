class employee:
    salary = 1200000
    language = 'english'   # class attribute

    def getinfo(self):
        print(f"This is a salary of {self.salary}")
    @staticmethod#it is use for show a dont use any self arrgurment
    def greet():
        print("good morning")

priyanshu = employee()
priyanshu.language = 'python'   # object instance attribute

priyanshu.getinfo()
priyanshu.greet()