class Vehicle:
    def __init__(self, brand, model, basic_performance):
        self._brand = brand
        self._model = model
        self._basic_performance = basic_performance

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    def performance(self):
        return self._basic_performance

    def __str__(self):
        return f"{self._brand} {self._model} | Performance: {self.performance():.2f}"


class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, basic_performance, battery_capacity, range_km):
        super().__init__(brand, model, basic_performance)
        self.battery_capacity = battery_capacity
        self.range_km = range_km

    def performance(self):
        return self._basic_performance + (self.range_km / 10) + (self.battery_capacity / 20)

    def __str__(self):
        return (f"EV - {super().__str__()} | Battery: {self.battery_capacity} kWh | "
                f"Range: {self.range_km} km")


class SportsCar(Vehicle):
    def __init__(self, brand, model, basic_performance, horsepower, acceleration):
        super().__init__(brand, model, basic_performance)
        self.horsepower = horsepower
        self.acceleration = acceleration

    def performance(self):
        return self._basic_performance + (self.horsepower / 10) - (self.acceleration * 2)

    def __str__(self):
        return (f"SportsCar - {super().__str__()} | HP: {self.horsepower} | "
                f"0-100: {self.acceleration}s")
