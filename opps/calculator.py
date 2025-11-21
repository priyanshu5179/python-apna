class calculator:
    def __init__(self, n):   # fixed: def __init__
        self.n = n

    def square(self):        # fixed: spelling & usage
        print(f"The square of the number is {self.n * self.n}")


a = calculator(45)   # fixed: class name was wrong (spuare)
a.square()           # fixed: method name was wrong (spuare)
