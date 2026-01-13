"""
Create a car class with attributes like brand and model. Then create an instance of this class.
"""

# class name should be capitalized
class Car:

    #constructor
    def __init__(self, brand, model): # self represents the the variable that has the object of the class
        self.brand = brand 
        self.model = model
        """
        - self.brand and self.model belongs to the Car class
        - brand and model are the parameters are being passed from the 
        variable that has an object of Car
        """
        

my_car = Car("BMW", "M8")
"""
- my_car is the instance of Car class
- my_car has an object of Car class. We can say my_car has a copy of Car() class.
- We are passing the brand and model through my_car variable.
"""

print(my_car.brand) # BMW
print(my_car.model) # M8