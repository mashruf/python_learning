"""
Modify the Car class to encapsulate the brand attribute, 
making it private, and provide a getter method for it. 
"""

class Car:

    def __init__(self, brand, model): 
        self.__brand = brand # private, used __ to make it private  
        self.model = model

    def get_brand(self): # getter method
        return self.__brand  # accessing the private variable brand      

    def full_name(self):
        return f'{self.brand} {self.model}'
    

class ElectricCar(Car):# inheriting
    def __init__(self, brand, model, battery_size): 

        super().__init__(brand, model)
        self.battery_size = battery_size

        

my_tesla = ElectricCar("Tesla", "S", "85kWh")

# print(my_tesla.brand) # we can not access the brand beccause its private

# print(my_tesla.__brand) # we can not access it either because private variable only acceessible inside class

print(my_tesla.get_brand()) # Tesla

"""
- We are able to access the private attribute brand only by the getter method.
- We will see setter method later
"""
