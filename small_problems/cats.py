class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    @property
    def info(self):
        return f'My {self.__class__.__name__.lower()} {self._name} is {self._age} years old and has {self._color} fur.'

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)