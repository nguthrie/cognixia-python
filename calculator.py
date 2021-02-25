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

def tests():
    '''
    First pass of tests for most functions.
    '''
    my_calc = Calculator()  # created an object from the class Calculator
    print(my_calc.add(1, 2))
    print(my_calc.last)     # 3

    # square of 3
    print(my_calc.exp(3, 2))
    print(my_calc.last)     # 9
    
    # store in memory
    my_calc.to_memory()
    print(my_calc.mem)      # 9 
    
    # new operation
    my_calc.subtract(10, 10)
    print(my_calc.last)     # 0

    # recall from mem
    my_calc.from_memory()
    print(my_calc.last)     # 9

    # square the number in memory
    my_calc.sqrt(my_calc.last)
    print(my_calc.last)     # 3

if __name__ == "__main__":

    # tests()
    
    my_calc2 = Calculator()

    continue_calc = True

    while continue_calc:

        if continue_calc == "N":
            break

        num1, comma, num2 = tuple(input("Please enter two comma seperated numbers: "))
        num1, num2 = float(num1), float(num2)
        print("1:Add\n2:Subtract\n3:Division\n4:Multiplcation\5:Exponent\6:Square Root")
        opp = int(input("Please enter a command number from above."))

        if opp == 1:
            print(my_calc2.add(num1, num2))
        
        continue_calc = input("Continue? y/N ")

        
        



