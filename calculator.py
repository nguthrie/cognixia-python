import math

class Calculator():

    last = None
    mem = None

    def add(self, x, y):
        self.last = x + y
        return self.last

    def subtract(self, x, y):
        self.last =  x - y
        return self.last

    def multiply(self, x, y):
        self.last =  x * y
        return self.last

    def division(self, x, y):
        self.last =  x / y
        return self.last

    def exp(self, x, y):
        self.last =  x**y
        return self.last

    def sqrt(self, x):
        self.last = math.sqrt(x)
        return self.last

    def to_memory(self):
        self.mem = self.last

    def from_memory(self):
        self.last = self.mem


if __name__ == "__main__":
    
    my_calc = Calculator()
    print(my_calc.add(1, 2))
    print(my_calc.last)
   
    # square of 3
    print(my_calc.exp(3, 2))
    print(my_calc.last)
    
    # store in memory
    my_calc.to_memory()
    print(my_calc.mem)
    
    # new operation
    my_calc.subtract(10, 10)
    print(my_calc.last)
   
    # recall from mem
    my_calc.from_memory()
    print(my_calc.last)
   
    # square the number in memory
    my_calc.sqrt(my_calc.last)
    print(my_calc.last)

