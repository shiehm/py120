class SignalMixin:
    def signal_left(self):
        print('Signaling left')
        
    def signal_right(self):
        print('Signaling right')
        
    def signal_off(self):
        print('Signal off')

class Vehicle(SignalMixin):
    counter = 0
    def __init__(self):
        Vehicle.counter += 1
    
    @classmethod
    def vehicles(cls):
        return Vehicle.counter

class Car(Vehicle):
    # Will work without this super init, good practice to have it
    def __init__(self):
        super().__init__()

class Truck(Vehicle):
    pass

class Boat(Vehicle):
    pass

print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8

car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'