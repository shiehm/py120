"""
Notes:
- A class called shelter is going to have a method adopt that accepts:
      - An argument for an object representing an Owner
      - An argument for an object representing a pet
- A class called Pet that takes 2 arguments: Animal Type and Name
- A class called Owner that takes a name argument of first initial and last name
      - attribute name = name
      - getter method for number_of_pets()
"""

class Pet:
      def __init__(self, animal, name):
            self.animal = animal
            self.name = name
            
      
      def info(self):
            return f'a {self.animal} named {self.name}'

class Owner:
      def __init__(self, name):
            self.name = name
            self.pets = []
      
      def add_pet(self, pet):
            self.pets.append(pet)
      
      def print_pets(self):
            for pet in self.pets:
                  print(pet.info())
      
      def number_of_pets(self):
            return len(self.pets)

class Shelter:
      def __init__(self):
            self.owners = []
            self.pets = []
      
      def adopt(self, owner, pet):
            if isinstance(owner, Owner) and isinstance(pet, Pet):
                  owner.add_pet(pet)
                  if owner not in self.owners:
                        self.owners.append(owner)
      
      def print_adoptions(self):
            for owner in self.owners:
                  print(f'{owner.name} has adopted the following pets:')
                  owner.print_pets()
                  print('')

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} adopted pets.")


"""
P Hanson has adopted the following pets:
a cat named Cocoa
a cat named Cheddar
a bearded dragon named Darwin

B Holmes has adopted the following pets:
a dog named Molly
a parakeet named Sweetie Pie
a dog named Kennedy
a fish named Chester

P Hanson has 3 adopted pets.
B Holmes has 4 adopted pets.
"""