"""
Create a Car class that meets these requirements:

- Each Car object should have a model, model year, and color provided at instantiation time.
- You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.
- Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.
- Create a method that prints a message about the car's current speed.
- Write some code to test the methods.
"""

from functools import total_ordering

@total_ordering
class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0
        self._engine = 0
    
    def __eq__(self, other):
        return self.model == other.model

    def __lt__(self, other):
        return self.year < other.year
    
    def __str__(self):
        return f'{self.model} {self.year} {self.color}'

    def __repr__(self):
        model = repr(self.model)
        year = repr(self.year)
        color = repr(self.color)
        return f'Car({model}, {year}, {color})'

    @staticmethod
    def drivers_manual():
        print('Here is a big manual.')
        print('Turn the car on first.')
        print('Accelerate and brake, then turn it off')
    
    @classmethod
    def mpg(cls, miles, gallons):
        if not isinstance(miles, int):
            raise TypeError('Must be integer')
        elif not isinstance(gallons, int):
            raise TypeError('Must be integer')
        return miles / gallons
    
    @property
    def model(self):
        return self._model
        
    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError('Color must be a string')
        self._color = new_color
    
    @property
    def speed(self):
        return self._speed

    def start_engine(self):
        self._engine = 1
        print('Starting engine')

    def off_engine(self):
        self._engine = 0
        self._speed = 0
        print('Engine off')

    def accelerate(self, amount):
        if self._engine == 0:
            print('Start the engine first!')
        elif self._engine == 1:        
            self._speed += amount
            print(f'Accelerating to {self.speed}')

    def brake(self, amount):
        if self.speed == 0:
            print('The car is not moving!')
        elif self.speed > 0:        
            self._speed -= amount
            print(f'Braking to {self.speed}')
            
    def paint_job(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError('Color must be a string')
        print(f'Painting the car to {new_color}!')
        self.color = new_color
        print(f'The car is now {self.color}!')

car1 = Car('Toyota', 1992, 'green')
car1.accelerate(10)
car1.brake(10)
car1.start_engine()
car1.accelerate(10)
car1.brake(5)
print(car1.speed)

print(car1.color)
car1.color = 'blue'
print(car1.color)

car1.off_engine()
print(car1.speed)

car1.paint_job('orange')
print(f'Testing the new color: {car1.color}')

print(f'MPG is {car1.mpg(100,10)}')
print(f'MPG is {Car.mpg(100,10)}')

car1.drivers_manual()
Car.drivers_manual()

car1 = Car('Toyota', 1992, 'Blue')
car2 = Car('Toyota', 1993, 'Blue')

print(car1)
print(repr(car1))
print(car1 < car2)
print(car2 > car1) # Issue here with functools