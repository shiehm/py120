"""
Note: The key is that gait needs to be called with () since it is a method, whereas
name is a variable and can be called without () notation. 

When you format a string in Python using f-string formatting and include an object 
within the braces (e.g., {self}), Python automatically invokes the __str__ method 
of that object for you. So, {self} within the f-string is essentially equivalent 
to invoking self.__str__

"""

class WalkingMixin:
    def walk(self):
        return f'{self} {self.gait()} forward'
        
        ## Can do it this way but the __str__ over-ride is more pythonic
        # if hasattr(self, 'title'):
        #     return f'{self.title} {self.name} {self.gait()} forward'
        # else:
        #     return f'{self.name} {self.gait()} forward'
    
    def __str__(self):
        return self.name

class Person(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"
    
class Cheetah(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
        
class Noble(WalkingMixin):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def gait(self):
        return "struts"
    
    def __str__(self):
        return f'{self.title} {self.name}'
    
    # def walk(self):
    #     return f'{self.title} {self.name} {self.gait()} forward'

mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

# print(hasattr(byron, 'gait'))
# print(getattr(byron, 'gait', ''))