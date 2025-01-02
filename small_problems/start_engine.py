class Vehicle:
    def __init__(self, year):
        self._year = year

    def start_engine(self):
        return 'Ready to go!'
        # print('Ready to go!')

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def __init__(self, year):
        super().__init__(year)
        print(super().start_engine())
    
    def start_engine(self, speed):
        return f'{super().start_engine()}! Drive {speed}, please!'

# Comments show expected output
truck1 = Truck(1992)
print(truck1.start_engine('fast'))
# Ready to go! Drive fast, please!

truck2 = Truck(1992)
print(truck1.start_engine('slow'))
# Ready to go! Drive slow, please!

# Comments show expected output
truck1 = Truck(1994)          # Ready to go!
print(truck1.year)            # 1994