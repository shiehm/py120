class TowMixin:
    def tow(self):
        print('I can tow a trailer!')

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Car(Vehicle):
    def __init__(self, year):
        super().__init__(year)

class Truck(Vehicle, TowMixin):
    def __init__(self, year, bed_type):
        super().__init__(year)
        self._bed_type = bed_type
    
    @property
    def bed_type(self):
        return self._bed_type

# Comments show expected output
truck1 = Truck(1994, 'Short')
print(truck1.year)            # 1994
print(truck1.bed_type)        # Short

car1 = Car(2006)
print(car1.year)              # 2006
try:
    print(car1.bed_type)
except:
    print('AttributeError: "Car" object has no attribute "bed_type"')

truck1.tow()        # I can tow a trailer!
try:
    car1.tow()
except AttributeError:
    print("AttributeError: 'Car' object has no attribute 'tow'")
