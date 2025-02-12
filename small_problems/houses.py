"""
You don't need to explicitly define __gt__ if you've defined __lt__. 
Python can automatically handle > operations by using your __lt__ method with 
the operands reversed. This is called "reflection" of comparison operators.


However, there are two things to keep in mind:
1. If you want to optimize performance, defining both __lt__ and __gt__ can be 
slightly faster as it avoids the reflection operation
2. If you want different logic for < and > (which is rare but possible), 
you would need to define both methods

In most cases though, just defining __lt__ is sufficient. Python will handle 
>, <=, and >= automatically through the @total_ordering decorator from the 
functools module or through reflection.
"""

class House:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __gt__(self, other):
        if isinstance(other, House):
            return self.price > other.price
        
        return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, House):
            return self.price < other.price
        
        return NotImplemented

home1 = House(100000)
home2 = House(150000)

if home1 < home2:
    print("Home 1 is cheaper")
if home2 > home1:
    print("Home 2 is more expensive")