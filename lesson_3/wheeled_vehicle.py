class VehicleMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency
    
    def number_validator(self, number):
        is_number = isinstance(number, int) or isinstance(number, float)
        is_digit = isinstance(number, str) and number.isdigit()
        return is_number or is_digit
    
    @property
    def fuel_capacity(self):
        return self._fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, fuel_capacity):
        if not self.number_validator(fuel_capacity):
            raise TypeError('Must be a number.')
        self._fuel_capacity = float(fuel_capacity)
    
    @property
    def fuel_efficiency(self):
        return self._fuel_efficiency
    
    @fuel_efficiency.setter
    def fuel_efficiency(self, fuel_efficiency):
        if not self.number_validator(fuel_efficiency):
            raise TypeError('Must be a number.')
        self._fuel_efficiency = float(fuel_efficiency)

class WheeledVehicle(VehicleMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)
        
class Boat(VehicleMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity
    
    def range(self):
        return super().range() + 10

class Catamaran(Boat):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity)

class Motorboat(Boat):
    def __init__(self, kilometers_per_liter, liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter, liters_of_fuel_capacity)


auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)
motorboat = Motorboat(2.0, 500)

print(auto.fuel_efficiency)             # 50
print(auto.fuel_capacity)               # 25.0
print(auto.range())                     # 1250.0

print(motorcycle.fuel_efficiency)       # 80
print(motorcycle.fuel_capacity)         # 8.0
print(motorcycle.range())               # 640.0

print(catamaran.fuel_efficiency)        # 1.5
print(catamaran.fuel_capacity)          # 600
print(catamaran.range())                # 900.0

print(motorboat.fuel_efficiency)        # 2.0
print(motorboat.fuel_capacity)          # 500
print(motorboat.range())                # 1,000.0