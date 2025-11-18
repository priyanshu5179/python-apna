class employee:
    salary = 1200000
    language = 'english'   # class attribute

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print('hi I am priyanshu')

    def getinfo(self):
        print(f"This is a salary of {self.salary}")


priyanshu = employee('hello', 12312312, 'english')
priyanshu.language = 'python'   # object instance attribute
print(priyanshu.salary,priyanshu.language) 
priyanshu=employee()