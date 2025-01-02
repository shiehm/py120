"""
The print function calls the __str__ method of the object passed to it to 
get a string representation of the object. 
Understanding this, we can override the __str__ method 
for any class to produce the desired output.
"""

class Cat:
    
    counter = 0
    COLOR = 'purple'
    
    def __init__(self, name, color="purple"):
        self.name = name
        self._color = color
        Cat.counter += 1

    def __str__(self):
        return f"I'm {self.name}"

    @classmethod
    def generic_greeting(cls):
        print('Hello, I am a Cat!')
    
    @classmethod
    def total(cls):
        return Cat.counter
    
    def personal_greeting(self):
        print(f"Hello! My name is {self.name}!")
    
    def greet(self):
        print(f"Hello! My name is {self.name} and I'm a {self._color} cat!")
        print(f"Hello! My name is {self.name} and I'm a {Cat.COLOR} cat!")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def rename(self, name):
        self.name = name
    
    def identify(self):
        return self
    
    # If using the getter method, need to call with () like .name()
    # def name(self):
    #     return self._name
    
kitty = Cat('Sophie')
kitty.greet()
kitty = Cat('Luna')
kitty.greet()

kitty.generic_greeting() # Not recommended to call cls methods via instance objects
Cat.generic_greeting()

print(type(kitty).generic_greeting())

kitty.rename('Chloe')
print(kitty.name)

print(kitty.identify())
print(kitty)
print(type(kitty))

kitty.personal_greeting()

print(Cat.total())
print(kitty)