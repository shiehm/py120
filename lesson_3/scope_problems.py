class Dog:
    def __init__(self, breed='default'):
        self.breed = breed
    
    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        self._breed = breed
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        if not isinstance(breed, str):
            raise TypeError('Breed must be a string.')
        self._breed = breed

    def __str__(self):
        return f'{self.breed}'
    
golden = Dog('Golden')
poodle = Dog('Poodle')

print(golden)
print(poodle)

golden.set_breed('Golden Retriever')
print(golden.get_breed())

new_dog = Dog()
new_dog.breed = 'CockadoodleDoo'
new_dog._breed = 'Lab'
print(new_dog)



class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return 'Name not set!!'
       
cat = Cat()
try:
    print(cat.get_name())
except:
    print('Name not set!')



class Student:
    
    school_name = 'Oxford'
    students = []
    
    def __init__(self, name):
        self.name = name
        Student.students.append(self)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_school_name(cls):
        return cls.school_name
    
bob = Student('bob')
claire = Student('Claire')

print(bob.name)
print(bob.school_name) # Not ideal to use instance to access class variable, b/c it's unclear that you are accessing a class variable
print(bob.__class__.school_name)
print(bob.__class__.__name__)
print('')

for student in Student.students:
    print(student)
    print(student.school_name)
    print(student.name)
    print(student.__class__.school_name)
    print(student.__class__.__name__)
    print(student.get_school_name())

print(Student.school_name)
print(Student.get_school_name())



class Car:
    manufacturer = 'Mitsubishi'
    
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def show_manufacturer(self):
        print('Class Variable: ', self.__class__.manufacturer)
        print('Class Variable: ', Car.manufacturer)
        print('Instance Variable: ', self.manufacturer)
        print()
        print(f'{self.__class__.manufacturer=}')
        print(f'{Car.manufacturer=}')
        print(f'{self.manufacturer=}')
        
toyota = Car('Toyota')
honda = Car('Honda')

toyota.show_manufacturer()
honda.show_manufacturer()



class Bird:
    def __init__(self, species):
        self.species = species
        
class Sparrow(Bird):
    def __init__(self, color):
        super().__init__('sparrow')
        self.color = color

sparrow = Sparrow('brown')
print(sparrow.species)
print(sparrow.color)



class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        self.legs = 2

print(Mammal().legs) # Mammal is the class, Mammal() is an instance, but not assigned to a vaariable
print(Human().legs)