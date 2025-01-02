class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._first_name + ' ' + self._last_name

    @name.setter
    def name(self, name):
        self._first_name = name.split()[0]
        self._last_name = name.split()[1] if len(name.split()) > 1 else ''
    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    def __str__(self):
        return self.name

    # def __eq__(self, other):
    #     return self.name == other.name
        
bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams

bob = Person('Robert Smith')
rob = Person('Robert Smith')

bob.name == rob.name

bob = Person('Robert Smith')
print(f"The person's name is: {bob}")