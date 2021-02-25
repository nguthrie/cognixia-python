class Car():

    wheels = 4
    doors = True

    def __init__(self, color, make, year, HP):
        self.color = color  #attributes
        self.make = make    #attributes
        self.year = year    #attributes
        self.HP = HP        #attributes

    # method 1
    def start_car(self):
        print("Veroom")

    def remove_wheel(self):
        self.wheels = self.wheels - 1

    def __gt__(self, other):
        return self.HP > other.HP

    def __str__(self):
        return self.make

my_car = Car("blue", "Ford", 2020, 150)
your_car = Car("red", "Tesla", 2020, 200)

my_car.wheels = 3

# my_car.start_car()

print(my_car < your_car)
print(my_car <= your_car)