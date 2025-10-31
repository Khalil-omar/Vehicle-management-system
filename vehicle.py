
# This is the main class of Vehicle

class Vehicle :
   
    def __init__(self,brand,model,basic_performance):
        self._brand = brand   # The Underscore is for protecting the attribute by convention that says “Please don’t modify me.”
        self._model = model
        self._basic_performance = basic_performance

    
    @property                  # The decorator is set to only Getter | Now it is protected
    def brand(self):
        return self._brand
    
    
    @property
    def model(self):
        return self._model
    
    def performance(self):
        return self._basic_performance
    

    def __str__(self):
        return f"{self._brand} {self._model} with Performance: {self.performance():.1f}"
    

# This is a subclass that represents the Sport Cars

class SportsCar(Vehicle):
    def __init__(self, brand, model, basic_performance,horse_power, accleration):
        super().__init__(brand, model, basic_performance)
        self._horse_power = horse_power
        self._acceleration = accleration

    # Performance Equation for sports cars [(basic performance + (horse power/100) + (acceleration*2)}
    def performance(self):
        return self._basic_performance + (self._horse_power/100) + (self._acceleration*2)
    
    def __str__(self):
        return f"SportsCar- {super().__str__()} | HP: {self.horsepower} | 0-100: {self.acceleration}s"



# This is a subclass that represents the Electric Cars
class ElectricCars(Vehicle):
    def __init__(self, brand, model, basic_performance, battery_capacity, range_km):
        super().__init__(brand, model, basic_performance)
        self._battery_capacity = battery_capacity
        self._range_km = range_km

    # Performance Equation for Electric cars [(basic performance + (battery capacity/10) + (range/100) }
    def performance(self):
        return self._basic_performance + (self._battery_capacity/10) + (self._range_km/100)

    def __str__(self):
        return f"Electric car- {super().__str__()} | battery capacity: {self._battery_capacity} with rane {self._range_km}"

