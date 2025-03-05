class Animal:
    def speak(self, message):
        if not isinstance(message, str):
            return NotImplemented
        print(message)

class Cat(Animal):
    def meow(self):
        self.speak('Meow!')

class Dog(Animal):
    def bark(self):
        # Can do this - this solution isn't the best:
        # self.__class__.speak(self, 'Woof! Woof! Woof!')

        # Or this:
        # super().speak('Woof! Woof! Woof!')

        # Or this - remember Dog inherits speak from Animal:
        self.speak('Woof! Woof! Woof!')
        
        # When you do this, you are invoking the Dog class, and it's missing the self, argument
        # self.__class__.speak('Woof! Woof! Woof!')