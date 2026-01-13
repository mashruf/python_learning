"""
Add a method to the Car class that displays the full name of the car.
"""

class Car:

    def __init__(self, brand, model): 
        self.brand = brand 
        self.model = model

    def full_name(self): # every method of a class must have self as parameter
        return f'{self.brand} {self.model}'
        

my_car = Car("BMW", "M8")

print(my_car.full_name()) # BMW M8