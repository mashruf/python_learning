"""
create an ElectricCar class that inherits from the Car class and has an additional 
attribute battery_size
"""

class Car:

    def __init__(self, brand, model): 
        self.brand = brand 
        self.model = model

    def full_name(self):
        return f'{self.brand} {self.model}'
    

class ElectricCar(Car):# inheriting
    def __init__(self, brand, model, battery_size): 
        """
        - battery_size is the new param for ElectricCar class
        - We must access brand and model from Car class
        """

        super().__init__(brand, model)
        """
        super() doing the following:
        
        self.brand = brand 
        self.model = model
        """
        
        self.battery_size = battery_size

        

my_tesla = ElectricCar("Tesla", "S", "85kWh")
print(my_tesla.full_name())  # Tesla S