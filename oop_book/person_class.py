class Person:
    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name) # Can access the setter 
    
    @classmethod
    def _validate(cls, name): # Strip out validation to a separate function, just as you would for a normal problem
        if not name.isalpha():
            raise TypeError('Names must be alphabetical')
    
    @property
    def name(self): # Can just return a string, doesn't need actual property called full name 
        return f'{self._first_name} {self._last_name}'
    
    @name.setter
    def name(self, new_name):
        first_name, last_name = new_name
        self._set_name(first_name, last_name)

    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name.capitalize()
        self._last_name = last_name.capitalize()

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
try:
    actor.name = ('', 'Diesel')
except:
    print('ValueError: Name must be alphabetic.')
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
try:
    character = Person('Da5id', 'Meier')
except:
    print('ValueError: Name must be alphabetic.')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
try:
    friend.name = ('Lynn', 'Blake-John')
except:
    print('ValueError: Name must be alphabetic.')
# ValueError: Name must be alphabetic.