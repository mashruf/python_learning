"""
Add a class variable to Car that keeps track of the
number of cars created.
"""

class Car:

    total_car = 0 # class variable

    def __init__(self, brand, model): 
        self.__brand = brand
        self.model = model
        Car.total_car += 1 # We use class variable by ClassName.Variable

    def get_brand(self):
        return self.__brand      

    def full_name(self):
        return f'{self.brand} {self.model}'
    
    def fuel_type(self): # polymorphism
        return "Petrol or Diesel"
    

class ElectricCar(Car):# inheriting
    def __init__(self, brand, model, battery_size): 

        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self): # polymorphism
        return "Electric Charge"
    

# Every time we create object of Car class, the class variable total_count will increas

Car("Tata", "Safari") # as we dont need the reference
Car("Toyota", "Corolla")

# We can access the class variable by following
print(Car.total_car) # 2

